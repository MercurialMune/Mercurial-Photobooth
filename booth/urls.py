from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^gallery/', views.gallery, name = 'gallery'),
    url('^locations/', views.locations_filter, name = 'locations'),
    url(r'^search/', views.search_results, name='search_results')
]
