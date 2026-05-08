# from django.urls import path
# from .views import TaskListCreateView

# urlpatterns = [
#     path('', TaskListCreateView.as_view()),
# ]

from django.urls import path
from .views import task_list

urlpatterns = [
    path('', task_list),
]