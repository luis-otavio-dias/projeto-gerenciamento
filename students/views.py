from django.shortcuts import render


# Create your views here.
def students(request):
    if request.method == "GET":
        return render(request, "students.html")
