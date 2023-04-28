from .models import Task
from django.forms import ModelForm, TextInput, Textarea, CharField, EmailField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your task'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            })
        }

    def save(self, commit=True, user=None):
        self.instance.user = user
        return super(TaskForm, self).save(commit=commit)


class NewUserForm(UserCreationForm):
    first_name = CharField(max_length=101)
    last_name = CharField(max_length=101)
    email = EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
