from .models import Census, Insurance, Total, Poverty, PopulationBySex
from rest_framework import routers, serializers, viewsets


class PopulationBySexSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationBySex
        fields = '__all__'


class CensusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Census
        fields = '__all__'


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'


class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = '__all__'


class PovertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Poverty
        fields = '__all__'
