from django.template import loader
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    text = 'Главная страница'
    context = {
        'text': text,
    }
    return render(request, template, context)

def group_posts(request):
    template = 'group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context)