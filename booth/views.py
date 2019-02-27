from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def gallery(request):
    return render (request, 'categories/all-images.html')


def education(request):
    return render (request, 'categories/education.html')


def entertainment(request):
    return render (request, 'categories/ entertainment.html'
                   )