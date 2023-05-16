from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Census, Insurance
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action
from rest_framework.response import Response

fs = FileSystemStorage(location='temp/')


class CensusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Census
        fields = '__all__'


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'


class CensusDataViewSet(viewsets.ModelViewSet):
    queryset = Census.objects.all()
    serializer_class = CensusSerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        file = request.FILES['file']
        content = file.read()
        file_content = ContentFile(content)
        file_name = fs.save('tmp.csv', file_content)
        tmp_file = fs.path(file_name)
        csv_file = open(tmp_file, errors='ignore')
        reader = csv.reader(csv_file)
        next(reader)

        census_list = []
        for id, row in enumerate(reader):
            (
                total_population,
                white_alone,
                black_or_african_american_alone,
                american_indian_and_alaskan_native_alone,
                asian_alone,
                native_hawaiian_and_other_pacific_islander_alone,
                other_race_alone,
                geo_id
            ) = row

            census_list.append(
                Census(
                    total_population=total_population,
                    white_alone=white_alone,
                    black_or_african_american_alone=black_or_african_american_alone,
                    american_indian_and_alaskan_native_alone=american_indian_and_alaskan_native_alone,
                    asian_alone=asian_alone,
                    native_hawaiian_and_other_pacific_islander_alone=native_hawaiian_and_other_pacific_islander_alone,
                    other_race_alone=other_race_alone,
                    geo_id=geo_id
                )
            )
        Census.objects.bulk_create(census_list)

        return Response("Census Data updated successfully")


class InsuranceDataViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        file = request.FILES['file']
        content = file.read()
        file_content = ContentFile(content)
        file_name = fs.save('tmp.csv', file_content)
        tmp_file = fs.path(file_name)
        csv_file = open(tmp_file, errors='ignore')
        reader = csv.reader(csv_file)
        next(reader)

        insurance_list = []
        for id, row in enumerate(reader):
            (
                age_category,
                people_insured,
                people_not_insured
            ) = row

            insurance_list.append(
                Insurance(
                    age_category=age_category,
                    people_insured=people_insured,
                    people_not_insured=people_not_insured
                )
            )
        Insurance.objects.bulk_create(insurance_list)

        return Response("Insurance Data updated successfully")
