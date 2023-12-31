from django.shortcuts import render, redirect, reverse
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
"""from django.http import HttpResponse

def zaglushka(request):
    return HttpResponse('Длмашка по 4 занятию! (у меня пропала папка с урока, так что пришлось делать всё заново)))')"""

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'lesson_4.index.html', context)

def top_sellers(request):
    return render(request, 'lesson_4.top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            return redirect(reverse('main-page'))

    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'lesson_4/advertisement-post.html', context)
