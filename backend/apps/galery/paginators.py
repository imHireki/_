from rest_framework import pagination
 

class IconPagination(pagination.PageNumberPagination):
    page_size = 20

