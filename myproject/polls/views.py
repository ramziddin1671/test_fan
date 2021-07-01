from django.shortcuts import render, HttpResponse
from .models import Category, Question, Choice
from django.core.paginator import Paginator
from django.views.generic import DetailView, TemplateView, ListView


class CategoryListView(ListView):
    model = Category
    template_name = "polls/home.html"


def category(request, category):
   questions = Question.objects.filter(category=category)
   return render(request, 'polls/question.html', {'questions': questions})


def check(request):
    result = ""
    for key, value in request.GET.items():
        choice = Choice.objects.get(pk=value)
        result += f"savolardan {key},<br>javobi: {choice.correct}<br><br>"
    return HttpResponse(result)

