from django.shortcuts import render
from .models import Image


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def gallery(request):
    images = Image.objects.all()
    return render(request, 'categories/all-images.html', {"images" : images})


def education(request):
    return render (request, 'categories/education.html')


def entertainment(request):
    return render (request, 'categories/entertainment.html')