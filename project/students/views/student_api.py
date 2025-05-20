from project.students.models import Students
from project.students.serializers import StudentsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


@api_view()
def students_list(request):
    students = Students.objects.all()
    serializer = StudentsSerializer(instance=students, many=True)
    return Response(serializer.data)


@api_view()
def student_detail(request, pk):
    student = get_object_or_404(
        Students.objects.filter(pk=pk),
    )
    serializer = StudentsSerializer(instance=student)
    return Response(serializer.data)
