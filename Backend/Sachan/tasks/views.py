# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from .models import Task
# from .serializers import TaskSerializer

# class TaskListCreateView(generics.ListCreateAPIView):
#     serializer_class = TaskSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Task.objects.all()

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all().values()

    return Response(list(tasks))