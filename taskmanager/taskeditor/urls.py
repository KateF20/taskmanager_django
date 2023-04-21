from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('', views.index, name='home'),
    path('delete', views.delete_task, name='delete_task')
]
