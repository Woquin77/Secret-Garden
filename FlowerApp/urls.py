from django.urls import path
from . import views

urlpatterns = [
    path('', views.flower_list, name='flowers'),
    path('add/', views.add_flower, name='add_flower'),
    path('edit/<int:id>/', views.edit_flower, name='edit_flower'),
    path('delete/<int:id>/', views.delete_flower, name='delete_flower'),
]