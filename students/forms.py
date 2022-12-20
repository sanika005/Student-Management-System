from django.forms import forms
from .models import Student

class StudentForm(forms.ModeForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'student_name': 'Student Name',
            'email': 'Student Email',
            'birth_date': 'Student D.O.B'
        }        