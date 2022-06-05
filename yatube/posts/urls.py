from django.urls import path
from . import views


app_name = 'homepage'

urlpatterns = [
    # Главная страница
    path('', views.index, name='home'),
    # Здесь можно всё
    path('group/<slug:slug>/', views.group_posts, name='group'),
]