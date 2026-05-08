# from django.urls import path
# from .views import register
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# urlpatterns = [
#     path('register/', register),
#     path('login/', TokenObtainPairView.as_view()),
#     path('refresh/', TokenRefreshView.as_view()),
# ]

# from django.urls import path

# from .views import (
#     register,
#     UserListView,
#     UserDetailView,
# )

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# urlpatterns = [

#     # AUTH
#     path(
#         'register/',
#         register
#     ),

#     path(
#         'login/',
#         TokenObtainPairView.as_view()
#     ),

#     path(
#         'refresh/',
#         TokenRefreshView.as_view()
#     ),

#     # USERS
#     path(
#         'users/',
#         UserListView.as_view()
#     ),

#     path(
#         'users/<int:pk>/',
#         UserDetailView.as_view()
#     ),
# ]

from django.urls import path

from .views import register,login,user_list

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path(
        'register/',
        register
    ),

    path(
    'login/',
    login
),
    path(
        'refresh/',
        TokenRefreshView.as_view()
    ),
    
path('users/', user_list),
]