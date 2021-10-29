from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

from .models import Icon
from .paginators import IconPagination
from .serializers import IconSerializer


class IconView(ListCreateAPIView):
    queryset = Icon.objects.all()
    serializer_class = IconSerializer
    pagination_class = IconPagination 
    
