# from django.shortcuts import render

# # Create your views here.
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from projects.models import Project
# from tasks.models import Task

# @api_view(['GET'])
# def dashboard_stats(request):
#     data = {
#         'projects': Project.objects.count(),
#         'tasks': Task.objects.count(),
#         'completedTasks': Task.objects.filter(status='done').count(),
#     }

#     return Response(data)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from projects.models import Project
from tasks.models import Task


@api_view(['GET'])
def dashboard_stats(request):

    data = {

        "stats": {
            "projects": Project.objects.count(),
            "tasks": Task.objects.count(),
            "completedTasks": Task.objects.filter(
                status='done'
            ).count(),
            "teamMembers": 1,
        },

        "byStatus": {
            "todo": Task.objects.filter(
                status='todo'
            ).count(),

            "in_progress": Task.objects.filter(
                status='in_progress'
            ).count(),

            "done": Task.objects.filter(
                status='done'
            ).count(),
        },

        "recentActivity": []
    }

    return Response(data)