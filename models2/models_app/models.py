from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length =50)
    address = models.CharField(max_length = 50)
    zip_code = models.IntegerField()

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length = 50)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Certificate_Type(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Grade(models.Model):
    grade_level= models.CharField(max_length = 50)

    def __str__(self):
        return self.grade_level


class Student(models.Model):
    full_name = models.CharField(max_length = 50)
    year_of_graduation = models.DateField(auto_now=datetime.year)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate_Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name