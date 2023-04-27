from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.main_page, name='main_page'),
    # path('stats/', views.summary_statistics, name='stats'),
]