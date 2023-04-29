from django.urls import path, re_path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('delete/<int:id>', views.delete_task, name='delete'),
    re_path(r'^(?P<status>all|completed|uncompleted)?$', views.index, name='home'),
]
