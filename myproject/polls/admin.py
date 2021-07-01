from django.contrib import admin
from .models import Category, Question, Choice


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "savol")


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "javob", "correct")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)