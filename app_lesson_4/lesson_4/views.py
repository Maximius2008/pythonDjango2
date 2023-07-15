from django.shortcuts import render
"""from django.http import HttpResponse

def zaglushka(request):
    return HttpResponse('Длмашка по 4 занятию! (у меня пропала папка с урока, так что пришлось делать всё заново)))')"""

def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')