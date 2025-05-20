from rest_framework import serializers
from project.students.models import Navigators


class StudentsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    navigator = serializers.StringRelatedField()
    stage = serializers.CharField()
    owner = serializers.CharField()
    created_in = serializers.DateField()
