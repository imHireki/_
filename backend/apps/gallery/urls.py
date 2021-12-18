"""
app gallery URL Configuration
"""
from django.urls import path
from . import views


urlpatterns = [
    path('icons/', views.IconView.as_view()),
    path('icons/image/', views.IconImageView.as_view()),
    path('icons/search/', views.SearchIconView.as_view()),
    path('icons/<slug:slug>/', views.IconDetailView.as_view()),
    ]

