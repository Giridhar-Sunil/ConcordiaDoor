from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_textbooks, name='search_textbooks'),
    path('<str:course_code>/', views.display_textbooks, name='display_textbooks'),
]
