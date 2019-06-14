from django import forms

from .models import Choice, Question, Instructor, Student, Secretary, Planning


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','password','hours']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'password']

class SecretaryForm(forms.ModelForm):
    class Meta:
        model = Secretary
        fields = ['name', 'password']

class PlanningForm(forms.ModelForm):
    class Meta:
        model = Planning
        fields = ['instructor', 'student', 'meeting_date', 'meeting_point', 'instructor_validation', 'student_validation']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['instructor', 'question_text', 'pub_date']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']
