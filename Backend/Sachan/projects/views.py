# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from .models import Project
# from .serializers import ProjectSerializer

# class ProjectListCreateView(generics.ListCreateAPIView):
#     serializer_class = ProjectSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Project.objects.all()

#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def project_list(request):

    data = [
        {
            "_id": 1,
            "name": "Pulse Project",
            "description": "My first project",
            "status": "active",
            "priority": "high",
        }
    ]

    return Response(data)