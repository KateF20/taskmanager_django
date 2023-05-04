from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^(?P<status>all|completed)?$', views.index, name='home'),
    path('create', views.create, name='create'),
    path('delete/<int:id>', views.delete_task, name='delete'),
    path('check_completed/<int:id>', views.check_completed, name='check_completed'),
    path('create_group', views.create_group, name='create_group'),
]
