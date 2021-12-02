"""
app gallery api views 
"""
from rest_framework.generics import (ListAPIView,
                                     ListCreateAPIView,
                                     CreateAPIView,
                                     GenericAPIView)
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework import status


from django.http import Http404

from .paginators import IconPagination
from .models import Icon, IconImage

from .serializers.image_upload import UploadIconImageSerializer
from .serializers.icon_list import IconSerializer


class IconView(ListAPIView):
    queryset = Icon.objects.all().select_related('user').prefetch_related('images')
    pagination_class = IconPagination 
    serializer_class = IconSerializer


class IconImageView(CreateAPIView):
    queryset = IconImage.objects.all()
    serializer_class = UploadIconImageSerializer


class SearchIconView(GenericAPIView):
    pagination_class = IconPagination
    serializer_class = IconSerializer

    def get_queryset(self):
        return Icon.objects.all(
            ).select_related('user').prefetch_related('images'
            ).filter(name__icontains=self.query)

    def get(self, request, format=None):
        self.query = request.GET.get('query', '')

        if not self.query:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.get_queryset() 

        if not queryset:
            return Response({'detail': 'no icons found'},
                            status=status.HTTP_404_NOT_FOUND
                            )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
