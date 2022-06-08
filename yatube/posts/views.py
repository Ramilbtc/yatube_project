from django.template import loader
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    text2 = f'Здесь будет информация о группах проекта Yatube {slug}'
    context = {
        'group_posts' : text2,
    }
    return render(request, template, context)