"""
core URL Configuration
"""
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    # Admin 
    path('admin/', admin.site.urls),

    # Djoser
    path('auth/', include('djoser.urls')),

    #TODO: REMOVE! DEV ONLY!
    path('api-auth/', include('rest_framework.urls')),
    ]

