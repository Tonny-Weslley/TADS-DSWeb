from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View

from .models import Choice, Question

# Create your views here.


class Index(View):
    def get(self, request, *args, **kwargs):
        Questions = Question.objects.all().order_by('-pub_date')[:25]
        context = {'Questions': Questions}
        return render(request, 'enquetes/pages/index.html', context)


class QuestionDetail(View):
    def get(self, request, *args, **kwargs):
        question_id = kwargs['question_id']
        question = get_object_or_404(Question, pk=question_id)
        context = {'question': question}
        return render(request, 'enquetes/pages/question_detail.html', context)


class QuestionResults(View):
    def get(self, request, *args, **kwargs):
        question_id = kwargs['question_id']
        question = get_object_or_404(Question, pk=question_id)
        context = {'question': question}
        return render(request, 'enquetes/pages/question_results.html', context)


class VoteView(View):
    def post(self, request, *args, **kwargs):
        question_id = kwargs['question_id']
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected = question.choice_set.get(pk=request.POST['choice_id'])
        except (KeyError, Question.DoesNotExist):
            contexto = {
                'question': question,
                'msg_erro': 'Selecione uma opção válida!'
            }
            return render(request, 'enquetes/pages/question_detail.html', contexto)
        else:
            selected.votes += 1
            selected.save()
            return HttpResponseRedirect(
                reverse('enquetes:question_results', args=(question.id,))
            )
