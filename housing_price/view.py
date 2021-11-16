from django.shortcuts import render


def home(request):
    context = {}
    context['content1'] = 'Hello World!'
    return render(request, 'home.html', context)