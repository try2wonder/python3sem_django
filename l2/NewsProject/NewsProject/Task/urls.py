from django.contrib import admin
from django.urls import path

from Task.views import index

urlpatterns = [
    path('', index)
]