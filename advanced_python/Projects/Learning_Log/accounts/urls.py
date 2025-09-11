"""Defines URL patterns for accounts."""
from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
app_name = 'accounts'
urlpatterns = [
    # include default auth urls
    path('',include('django.contrib.auth.urls')),
    # Registration Page
    path('register/',views.register,name='register'),
    # Logout Page
    path('logout/',LogoutView.as_view(),name='logout'),
    
]
