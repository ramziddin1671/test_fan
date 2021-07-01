from django.urls import path, include
from django.conf import settings
from . import views

app_name = 'polls'
urlpatterns = [
    path("",  views.CategoryListView.as_view(), name="home"),
    path('question/<int:category>/', views.category, name="question"),
    path('check/', views.check, name='check'),


]
