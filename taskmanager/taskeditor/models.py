from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField('Title', max_length=50)
    task = models.TextField('Description')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tasky'
        verbose_name_plural = 'Taskies'
