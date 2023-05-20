from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.index, name='index'),
    path('api/events/', views.all, name='all'),
    path('api/events/add', views.add, name='add'),
]