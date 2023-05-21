from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.index, name='index'),
    path('api/events/', views.all, name='all'),
    path('api/events/<int:id>', views.get, name='get'),
    path('api/events/add', views.add, name='add'),
    path('api/events/update/<int:id>', views.update, name='update'),
    path('api/events/delete/<int:id>', views.delete, name='delete'),
]