"""
app galery api views 
"""
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .paginators import IconPagination
from .serializers import IconSerializer
from .models import Icon


class IconView(ListCreateAPIView):
    queryset = Icon.objects.all().select_related('user')
    serializer_class = IconSerializer
    pagination_class = IconPagination 
    
