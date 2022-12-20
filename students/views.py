from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse

# Two types of views:
# 1. Function based view
# 2. Class based view 
# We will use function based view
def index(request):
    students_details = Student.objects.all()
    context = {'students':students_details}
    return render(request, 'students/index.html',context)

def view_student(request,id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))