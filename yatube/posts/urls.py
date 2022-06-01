from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Здесь можно всё
    path('group/<slug:slug>/', views.group_posts),
] 
