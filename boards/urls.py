from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # :8080/boards/
    path('new/', views.new),
    path('create/', views.create),
    path('detail/<int:pk>/', views.detail),
    path('delete/<int:pk>/', views.delete),
    path('edit/<int:pk>/', views.edit),
    path('update/<int:pk>/', views.update),
]