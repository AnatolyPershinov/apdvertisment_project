from django.contrib.auth import get_user_model
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required

User = get_user_model()


def index(request):
    return render(request, 'app_advertisements/index.html')


def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {
        'advertisement': advertisement,
    }
    return render(request, 'app_advertisements/advertisement.html', context)



@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)
