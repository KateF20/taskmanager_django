from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='taskeditor'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('home', views.home, name='home')
]
