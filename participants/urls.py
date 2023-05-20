from django.urls import path
from . import views

urlpatterns = [
    path('participants/', views.index, name='index'),
    path('api/participants', views.list, name='list'),
]