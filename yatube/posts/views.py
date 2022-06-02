from django.http import HttpResponse


def index(request):
    return HttpResponse(f'Главная страница')

def group_posts(request, slug):
    return HttpResponse(f'Посты {slug}')
