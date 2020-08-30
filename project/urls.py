from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="HomePage"),
    path('create/', views.create, name="create"),
    path('search-results/', views.search_results, name='search'),
]
