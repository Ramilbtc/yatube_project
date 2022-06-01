from django.http import HttpResponse


def group_posts(request, slug):
    return HttpResponse(f'= {slug} =')

def group_posts(request):
    return HttpResponse('Здесь можно всё')
