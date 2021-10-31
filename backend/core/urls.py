"""
core URL Configuration
"""
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

import debug_toolbar


urlpatterns = [
    # Admin 
    path('admin/', admin.site.urls),

    # Djoser
    path('auth/', include('djoser.urls')),

    #TODO: REMOVE! rest framework auth 
    path('api-auth/', include('rest_framework.urls')),

    #TODO: REMOVE! Debug Toolbar
    path('__debug__/', include(debug_toolbar.urls)),

    # Api v1
    path('api/v1/', include('apps.galery.urls')),

    # MEDIA: Bind media URL to its files 
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

