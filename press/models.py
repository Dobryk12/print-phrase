from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Topic(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=266)
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(get_user_model(), related_name='newspapers')

    class Meta:
        ordering = ['-published_date',]
