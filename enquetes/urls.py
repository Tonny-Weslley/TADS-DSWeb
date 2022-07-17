from django.urls import path

from . import views

app_name = 'enquetes'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('enquete/<int:question_id>/',
         views.QuestionDetail.as_view(), name='question_detail'),
    path('enquente/results/<int:question_id>/',
         views.QuestionResults.as_view(), name='question_results'),
    path('enquete/vote/<int:question_id>/',
         views.VoteView.as_view(), name='vote'),
]
