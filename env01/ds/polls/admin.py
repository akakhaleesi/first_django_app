from django.contrib import admin

from .models import Question, Choice, Instructor, Student, Secretary, Vote, Planning

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Secretary)
admin.site.register(Vote)
admin.site.register(Planning)
