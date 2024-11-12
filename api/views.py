from django.shortcuts import render
from django.contrib.auth import login, authenticate
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import viewsets
from .models import Department, Position, Employee
from .serializers import *
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnlyForUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['GET','POST','DELETE','PUT'])
@permission_classes([IsAdminOrReadOnlyForUser])
def example_view(request):
    if request.method == 'GET':
        return Response ({"message": "GET request success!"})
                         

    elif request.method == 'POST':
        return Response ({"message": "POST request success!"})


    elif request.method == 'PUT':
        return Response ({"message": "PUT request success!"})
    
    elif request.method == 'DELETE':
        return Response ({"message": "DELETE request success!"})


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer  # You need to create a UserSerializer

    
