from django.forms import model_to_dict
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task, Store
from .serializers import TaskSerializer


class TaskAPIView(APIView):
    def post(self, request):
        store_id = request.data.get('store')
        store_instance = get_object_or_404(Store, id=store_id)

        new_task = Task.objects.create(
            task_type=request.data['task_type'],
            task_name=request.data['task_name'],
            task_description=request.data['task_description'],
            task_members=request.data['task_members'],
            date_creation=request.data['date_creation'],
            days_to_complete=request.data['days_to_complete'],
            store=store_instance,
        )
        return Response({'message': model_to_dict(new_task)})

    def get(self, request):
        task = Task.objects.all()
        return Response({'Task': TaskSerializer(task, many=True).data})

    def patch(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(instance=task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task updated successfully'})
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task updated successfully'})
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response({'message': 'Task deleted successfully'})
