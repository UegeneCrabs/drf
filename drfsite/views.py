from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Task, Store
from .permissions import CustomPermission
from .serializers import TaskSerializer, StoreSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (CustomPermission,)
    #authentication_classes = (TokenAuthentication,)

    # ------------------------------8:9 lesson-------------------------#
    @action(methods=['get'], detail=False)
    def store(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response({'stores': serializer.data})

# ------------------------------other lesson-------------------------#
