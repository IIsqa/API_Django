from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.

# @api_view(['GET', 'POST'])
# def department_list(request):
#     if request.method == 'GET':
#         departments = Department.objects.all()
#         serializer = DepartmentSerializer(departments, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = DepartmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentListCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    allowed_methods = ['GET', 'POST']

    # def delete(self, request, *args, **kwargs):
    #     Department.objects.all().delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class DepartmentRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'pk'
    allowed_methods = ['PUT','DELETE']



class DepartmentDetailView(APIView):
    def get(self, request, name=None):
        if name:
            department = Department.objects.filter(name__icontains=name)
        else:
            department = Department.objects.all()

        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class PositionListCreate(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    allowed_methods = ['GET', 'POST']

    # def delete (self, request,*args, **kwargs):
    #     Position.objects.all().delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



class PositionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    allowed_methods = ['DELETE', 'PUT']
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    lookup_field = 'pk'



class PositionDetailView(APIView):
    def get(self, request, name=None):
        if name:
            position = Position.objects.filter(name__icontains=name)
        else:
            position = Position.objects.all()

        serializer = PositionSerializer(position, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def delete (self, request,*args, **kwargs):
        Position.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)