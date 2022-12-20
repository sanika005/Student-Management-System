from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=6)
    mobile_no = models.CharField(max_length=12)

    def __str__(self):
        return f'Student: {self.student_name}'
