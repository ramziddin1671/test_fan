from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categories"

    def __str__(self):
        return self.name


class Question(models.Model):
    savol = models.CharField(max_length=500, verbose_name="savollar")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.savol


class Choice(models.Model):
    javob = models.CharField(max_length=500, verbose_name="javobllar")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField()

    def __str__(self):
        return self.javob