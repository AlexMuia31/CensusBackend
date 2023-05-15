from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Census
# Create your views here.


class CensusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Census
        fields = '__all__'


class CensusDataViewSet(viewsets.ModelViewSet):
    queryset = Census.objects.all()
    serializer_class = CensusSerializer
