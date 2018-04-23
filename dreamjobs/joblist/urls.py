from django.urls import path
from django.contrib.auth import views
from .views import *

urlpatterns = [
    path('', job_list, name='job'),
]
