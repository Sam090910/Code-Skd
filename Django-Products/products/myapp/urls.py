from django.urls import path

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage")
]
