from posts import views
from django.contrib import admin
from posts import views
from django.urls import path

app_name = "posts"

urlpatterns = [
    path('', views.news, name = "news"),
    path('page/<int:page_number>', views.news, name = "page_news"),
    path('advertisements', views.advertisements, name = "advertisements"),
    path('advertisements/<int:advertisement_id>', views.one_advertisement, name = "advertisement"),
    path('create_advertisements', views.create_advertisements, name = 'create_advertisements'),
    path('create_offer', views.create_offer, name = 'create_offer'),
]
