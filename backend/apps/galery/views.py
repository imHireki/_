"""
app galery api views 
"""
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import Http404

from .paginators import IconPagination
from .models import Icon, IconImage

from .serializers.image_upload import UploadIconImageSerializer
from .serializers.icon_list import IconSerializer


class IconView(ListAPIView):
    queryset = Icon.objects.all().select_related('user').prefetch_related('images')
    pagination_class = IconPagination 
    serializer_class = IconSerializer

class IconImageView(ListCreateAPIView):
    queryset = IconImage.objects.all()
    serializer_class = UploadIconImageSerializer

