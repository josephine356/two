from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    '''
    Render the main page
    '''
    html = '''
    <!doctype html>
    <html>
    <head>
    <title>部落格</title>
    <meta charset="utf-8">
    </head>
    <body>
    <p>這是 HTML 版的 Hello world!</p>
    </body>
    </html>
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'main/main.html', context)

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')

def registered(request):
    '''
    Render the registered page
    '''
    return render(request, 'main/registered.html')

def login(request):
    '''
    Render the login page
    '''
    return render(request, 'main/login.html')
