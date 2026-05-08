# from django.shortcuts import render

# # Create your views here.
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import RegisterSerializer

# @api_view(['POST'])
# def register(request):
#     serializer = RegisterSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated

# from .serializers import (
#     RegisterSerializer,
#     UserSerializer
# )

# from .models import User


# @api_view(['POST'])
# def register(request):

#     serializer = RegisterSerializer(
#         data=request.data
#     )

#     if serializer.is_valid():
#         serializer.save()

#         return Response(
#             serializer.data,
#             status=status.HTTP_201_CREATED
#         )

#     return Response(
#         serializer.errors,
#         status=status.HTTP_400_BAD_REQUEST
#     )


# class UserListView(generics.ListAPIView):

#     queryset = User.objects.all()

#     serializer_class = UserSerializer

#     permission_classes = [IsAuthenticated]


# class UserDetailView(
#     generics.RetrieveUpdateDestroyAPIView
# ):

#     queryset = User.objects.all()

#     serializer_class = UserSerializer

#     permission_classes = [IsAuthenticated]

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import User


@api_view(['POST'])
def register(request):

    try:

        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(
            username=username
        ).exists():

            return Response(
                {'detail': 'Username already exists'},
                status=400
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
        })

    except Exception as e:

        return Response(
            {'detail': str(e)},
            status=500
        )
        
        
@api_view(['POST'])
def login(request):

    email = request.data.get('email')

    password = request.data.get('password')

    try:

        user_obj = User.objects.get(
            email=email
        )

    except User.DoesNotExist:

        return Response(
            {
                'detail': 'Invalid credentials'
            },
            status=401
        )

    user = authenticate(
        username=user_obj.username,
        password=password
    )

    if user is None:

        return Response(
            {
                'detail': 'Invalid credentials'
            },
            status=401
        )

    from rest_framework_simplejwt.tokens import RefreshToken

    refresh = RefreshToken.for_user(user)

    return Response({

        'access': str(
            refresh.access_token
        ),

        'refresh': str(refresh),
    })        
        
@api_view(['GET'])
def user_list(request):
    users = User.objects.all().values(
        'id',
        'username',
        'email'
    )

    return Response(list(users))        