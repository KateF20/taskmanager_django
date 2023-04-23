from django.contrib import admin
from django.urls import path, include
from taskmanager.taskeditor.views import registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('taskmanager.taskeditor.urls')),
    path('registration', registration, name='registration')
]
