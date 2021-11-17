"""
app galery api views 
"""
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .paginators import IconPagination
from .serializers import IconSerializer, IconImageSerializer
from .models import Icon, IconImage


class IconView(ListCreateAPIView):
    queryset = Icon.objects.all().select_related('user').prefetch_related('images')
    pagination_class = IconPagination 
    serializer_class = IconSerializer

class IconImageView(APIView):
    def post(self, request, format=None):
        image = request.data.get('image', None)
        serializer = IconImageSerializer(data={'image': image})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

