from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Task, Store
from .permissions import CustomPermission
from .serializers import TaskSerializer, StoreSerializer


class MyPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (CustomPermission,)
    # authentication_classes = (TokenAuthentication,)
    pagination_class = MyPagination

    @action(methods=['get'], detail=False)
    def store(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response({'stores': serializer.data})
