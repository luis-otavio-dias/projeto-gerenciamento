from rest_framework import serializers
from project.students.models import Students, Task


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ["id", "name", "navigator", "stage", "owner", "created_in"]

    navigator = serializers.StringRelatedField()
    owner = serializers.CharField()


class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields = ["id", "student", "task", "executed"]

    student = serializers.StringRelatedField()
    student_link = serializers.HyperlinkedRelatedField(
        source="student",
        queryset=Students.objects.all(),
        view_name="students:student_detail",
    )
    task = serializers.CharField()
    executed = serializers.BooleanField(read_only=True)
