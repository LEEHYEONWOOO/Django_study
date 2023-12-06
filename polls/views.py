from django.http import HttpResponse
from django.views.generic import ListView

from django.views import generic

from general.models import Employee
from .models import Choice, Question
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import QuerySet
from . import forms
from django.views.generic import TemplateView


class index_view(TemplateView):
    template_name = 'polls/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emp'] = Employee.objects.all()
        return context


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        if self.queryset is None:
            if self.model:
                return self.model._default_manager.all()
            else:
                return None  # origin : ImproperlyConfigured()

    def get_template_names(self):
        if self.template_name is None:
            return None  # origin :  ImproperlyConfigured()
        else:
            # return None
            return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object1'] = Choice.objects.filter()
        context['object2'] = self.model.objects.filter()
        qs = Question.objects.exclude(pk=self.object.pk)
        init = {'queryset': qs}
        context['form'] = forms.question_form(initial=init)
        return context


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"




def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



def create_q(request):
    if request.method == 'POST':
        form = forms.question_model_form
        if form.is_valid():
            form.save()
    else:
        form = forms.question_model_form
        return render(request, 'create_q.html', {'form': form})







