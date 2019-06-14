from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/form/', views.StudentForm.as_view(), name='student_form'),
    path('plannings/', views.PlanningListView.as_view(), name='planning_list'),
    path('plannings/<int:pk>', views.PlanningDetailView.as_view(), name='planning_detail'),
    path('plannings/form/', views.PlanningForm.as_view(), name='planning_form'),
    path('questions/form/', views.QuestionForm.as_view(), name='question_form'),
    path('choice/form/', views.ChoiceForm.as_view(), name='choice_form'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('register/', views.RegisterView, name='register'),
]
