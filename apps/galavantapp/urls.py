from django.conf.urls import url, include
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^trail/(?P<id>\d+)$', views.trail),
    url(r'^half_dome$', views.half_dome)
]
