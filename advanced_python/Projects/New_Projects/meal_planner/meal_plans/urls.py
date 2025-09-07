"""Define URL patterns for meal_plans app."""
from django.urls import path
from . import views

app_name = 'meal_plans'
urlpatterns = [
    path('', views.index, name='index'),
]