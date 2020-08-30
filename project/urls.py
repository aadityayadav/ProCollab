from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.empty, name="HomePage"),
    path('create/', views.create, name="create"),
    path('index/', views.index, name='index'),
    path('discover/', views.discover, name='discover'),
    path('search-results/', views.search_results, name='search'),
]
