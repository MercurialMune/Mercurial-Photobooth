from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^gallery/', views.gallery, name = 'gallery'),
    url('^education/', views.education, name = 'education'),
    url('^entertainment/', views.entertainment, name = 'entertainment'),

]
