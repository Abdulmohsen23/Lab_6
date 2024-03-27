from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 64)
    symbol = models.CharField(max_length = 5)

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class Student(models.Model):
    first = models.CharField(max_length = 64)
    last = models.CharField(max_length = 64)
    gpa = models.FloatField()
    age = models.IntegerField()
    courses = models.ManyToManyField(Course, blank=True, related_name="students")

    def __str__(self):
        return f"{self.first} {self.last}"