from django.urls import path
from . import views


urlpatterns = [
    path('icons/', views.IconView.as_view())
    ]

