from django.http import  HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic

# Create your views here.
from django.urls import reverse, reverse_lazy

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class QuestionCreate(generic.CreateView):
    model = Question
    fields = '__all__'
    # 2022-05-18 14:37:06

    def get_success_url(self):
        return reverse('polls:detail', kwargs={'pk': self.object.pk})


class QuestionUpdate(generic.UpdateView):
    model = Question
    fields = '__all__'

    def get_success_url(self):
        return reverse('polls:detail', kwargs={'pk': self.object.pk})


class QuestionDelete(generic.DeleteView):
    model = Question
    success_url = reverse_lazy('polls:index')


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'Yout didn\'t select a choice'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))

