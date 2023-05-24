from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField('Name', max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'


class Task(models.Model):
    title = models.CharField('Title', max_length=50)
    task = models.TextField('Description')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tasky'
        verbose_name_plural = 'Taskies'
