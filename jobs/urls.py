from django.urls import path
from . import views

urlpatterns = [
    path('', views.name),
    path('result/', views.result),
]