from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_registration, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile_update', views.profile_update, name='profile_update')
]
