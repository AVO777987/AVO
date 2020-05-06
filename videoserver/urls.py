from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('edit/', views.edit, name='edit'),
    path('update/', views.update, name='update'),
    path('create/', views.create, name='create')
]