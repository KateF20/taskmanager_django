from .models import Task
from django.forms import ModelForm, TextInput, Textarea


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
        self.cleaned_data['user'] = user
        return super(TaskForm, self).save(commit=commit)