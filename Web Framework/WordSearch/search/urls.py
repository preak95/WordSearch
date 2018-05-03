from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.search, name="search"),
    url(r'^search/', views.search, name="search")
]