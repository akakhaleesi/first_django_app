from django.db import models
from django.urls import reverse
from django.forms import ModelForm
from datetime import datetime


class Instructor(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200, default='toto')
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200, default='toto')
    hours =  models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})

class Secretary(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200, default='toto')
    def __str__(self):
        return self.name

class Question(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text

class Planning(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    meeting_date = models.DateTimeField('appointment')
    meeting_point = models.CharField(max_length=200)
    instructor_validation = models.IntegerField(default=0)
    student_validation = models.IntegerField(default=0)
    def __str__(self):
        return self.meeting_date
