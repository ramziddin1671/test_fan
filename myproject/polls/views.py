from django.shortcuts import render, HttpResponse
from .models import Category, Question, Choice
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class CategoryListView(ListView):
    model = Category
    template_name = "polls/home.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoryListView, self).dispatch(*args, **kwargs)


def category(request, category):
   questions = Question.objects.filter(category=category)
   return render(request, 'polls/question.html', {'questions': questions})


def check(request):
    question_num = []
    answers = []
    for key, value in request.GET.items():
        question_num.append(key)
        answers.append(int(value))

    questions = Question.objects.filter(id__in=question_num)
    return render(request, 'polls/question.html', {'questions': questions, "answers": answers})


