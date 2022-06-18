from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'lastest_question_list': lastest_question_list, }
    return render(request, 'enquetes/index.html', context)

def detail(request, question_id):
    response = "Você está visualizando a questão %s."
    return HttpResponse(response % question_id)

def results(request, question_id):
    response = "Resultados da questão %s."
    return HttpResponse(response % response)

def vote(request, question_id):
    response = "Votação da questão %s."
    return HttpResponse(response % response)