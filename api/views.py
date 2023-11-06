from django.shortcuts import render
from rest_framework.views import APIView
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.filters import OrderingFilter

# Create your views here.
class Studentlist(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def filter_queryset(self, queryset):
        name = self.request.query_params.get('name')
        age = self.request.query_params.get('age')
        address = self.request.query_params.get('address')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if age:
            queryset = queryset.filter(age=int(age))
        if address:
            queryset = queryset.filter(address__icontains=address)

        return super().filter_queryset(queryset)

    
        
