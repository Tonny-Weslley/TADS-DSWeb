"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

import enquetes

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
