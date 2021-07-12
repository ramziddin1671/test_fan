from django.shortcuts import render, HttpResponse
from .models import Category, Question, Choice, Result
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CategoryListView(ListView):
    model = Category
    template_name = "polls/home.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoryListView, self).dispatch(*args, **kwargs)


class ResultListView(ListView):
    template_name = 'polls/account.html'

    def get_queryset(self):
        return Result.objects.filter(user_id=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ResultListView, self).dispatch(request, *args, **kwargs)


class QuestionListView(ListView):
    template_name = 'polls/question.html'

    def get_queryset(self):
        return Question.objects.filter(category=self.kwargs['category'])

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(QuestionListView, self).dispatch(request, *args, **kwargs)


@login_required
def category(request, category):
   questions = Question.objects.filter(category=category)
   return render(request, 'polls/question.html', {'questions': questions})


@login_required
def check(request):
    user = request.user
    answers = []
    question_numbers = []
    for key, value in request.GET.items():
        question_numbers.append(int(key))
        answers.append(int(value))

    questions = Question.objects.filter(id__in=question_numbers)
    choices = Choice.objects.filter(id__in=answers)

    correct_answers = 0
    for ch in choices:
        if ch.correct:
            correct_answers += 1
    result = (correct_answers / len(answers) * 100)

    Result.objects.update_or_create(
        user_id=user, category=questions[0].category,
        defaults={
            'user_id': user,
            'category': questions[0].category,
            'result': result},
    )

    return render(request, 'polls/check.html',
                  {'questions': questions,
                   'answers': answers,
                   'result': result})


