from django.shortcuts import render
from .models import Image, Category, Location


def welcome(request):
    return render(request, 'welcome.html')


def gallery(request):
    all_locations = Location.objects.all()
    images = Image.objects.all()
    return render(request, 'categories/all-images.html', {"all_locations": all_locations, "images": images})


def search_results(request):
    all_locations = Location.objects.all()
    all_categories = Category.objects.all()
    if 'category' in request.GET and request.GET["category"]:
        parameter = request.GET.get("category")
        img = Image.search_image(parameter)
        message = f"{parameter}"
        return render(request, 'categories/search.html',
                      {"message": message, "category": img, "all_locations": all_locations,
                       "all_categories": all_categories})

    else:
        message = "null"
        return render(request, 'categories/search.html',
                      {"message": message, "all_categories": all_categories, "all_locations": all_locations})


def locations_filter(request):
    all_locations = Location.objects.all()
    location = request.GET.get("location")
    select_location = Image.filter_by_location(location)
    message = f'{location}'
    return render(request, 'categories/location.html',
                  {"message": message, "all_locations": all_locations, "location": select_location})
