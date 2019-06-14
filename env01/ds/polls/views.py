from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.forms import modelformset_factory
from django.views import generic
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView

from .models import Choice, Question, Instructor, Student, Secretary, Planning
from polls.forms import StudentForm, PlanningForm, QuestionForm, ChoiceForm


class StudentListView(generic.ListView):
    template_name = 'polls/student_list.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        """Return students."""
        return Student.objects.order_by('-name')[:50]

class PlanningListView(generic.ListView):
    template_name = 'polls/planning_list.html'
    context_object_name = 'planning_list'

    def get_queryset(self):
        return Planning.objects.order_by('-meeting_date')[:50]

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:50]

class StudentForm(FormView):
    template_name = 'polls/student_form.html'
    form_class = StudentForm
    success_url = '/polls/students/'

    def form_valid(self, form):
        form.save()
        return HttpResponse('success')

class PlanningForm(FormView):
    template_name = 'polls/planning_form.html'
    form_class = PlanningForm
    success_url = '/polls/plannings/'

    def form_valid(self, form):
        id = form.cleaned_data['student']
        student = Student.objects.get(name=id)
        print(student.hours)
        if student.hours < 1:
            return HttpResponse('no hours left')
        else:
            form.save()
            return HttpResponse('success')

class QuestionForm(FormView):
    template_name = 'polls/question_form.html'
    form_class = QuestionForm
    success_url = '/polls/'

    def form_valid(self, form):
        form.save()
        return HttpResponse('success')

class ChoiceForm(FormView):
    template_name = 'polls/choice_form.html'
    form_class = ChoiceForm
    success_url = '/polls/'

    def form_valid(self, form):
        form.save()
        return HttpResponse('success')

def RegisterView(request):
    return render(request, 'polls/register.html')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'polls/student_detail.html'

class StudentFormView(generic.DetailView):
    model = StudentForm
    template_name = 'polls/student_form.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class PlanningDetailView(generic.DetailView):
    model = Planning
    template_name = 'polls/planning_detail.html'

class PlanningFormView(generic.DetailView):
    model = PlanningForm
    template_name = 'polls/planning_form.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
