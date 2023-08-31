from django.shortcuts import render
from rest_framework import viewsets
from .models import Census, Insurance, Total, Poverty, PopulationBySex
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PopulationBySexSerializer, CensusSerializer, InsuranceSerializer, TotalSerializer, PovertySerializer

fs = FileSystemStorage(location='temp/')


def process_csv(file):
    content = file.read()
    file_content = ContentFile(content)
    file_name = fs.save('tmp.csv', file_content)
    tmp_file = fs.path(file_name)
    csv_file = open(tmp_file, errors='ignore')
    reader = csv.reader(csv_file)
    next(reader)
    return reader


class CensusDataViewSet(viewsets.ModelViewSet):
    queryset = Census.objects.all()
    serializer_class = CensusSerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        file = request.FILES['file']
        reader = process_csv(file)

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
        reader = process_csv(file)

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


class TotalDataViewSet(viewsets.ModelViewSet):
    queryset = Total.objects.all()
    serializer_class = TotalSerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        file = request.FILES['file']
        reader = process_csv(file)

        total_list = []
        for id, row in enumerate(reader):
            (
                total_population,
                white_alone,
                black_or_african_american_alone,
                american_indian_and_alaskan_native_alone,
                asian_alone,
                native_hawaiian_and_other_pacific_islander_alone,
                other_race_alone,
                two_or_more_races,
                other,
                median_household_income
            ) = row

            total_list.append(
                Total(
                    total_population=total_population,
                    white_alone=white_alone,
                    black_or_african_american_alone=black_or_african_american_alone,
                    american_indian_and_alaskan_native_alone=american_indian_and_alaskan_native_alone,
                    asian_alone=asian_alone,
                    native_hawaiian_and_other_pacific_islander_alone=native_hawaiian_and_other_pacific_islander_alone,
                    other_race_alone=other_race_alone,
                    two_or_more_races=two_or_more_races,
                    other=other,
                    median_household_income=median_household_income
                )
            )
        Total.objects.bulk_create(total_list)

        return Response("Total Data updated successfully")


class PovertyViewSet(viewsets.ModelViewSet):
    queryset = Poverty.objects.all()
    serializer_class = PovertySerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        file = request.FILES['file']
        reader = process_csv(file)

        poverty_list = []
        for id, row in enumerate(reader):
            (
                all_ages_in_poverty,
                ages_5_to_17_in_poverty,
                ages_0_17_in_poverty
            ) = row

            poverty_list.append(
                Poverty(
                    all_ages_in_poverty=all_ages_in_poverty,
                    ages_5_to_17_in_poverty=ages_5_to_17_in_poverty,
                    ages_0_17_in_poverty=ages_0_17_in_poverty
                )
            )
        Poverty.objects.bulk_create(poverty_list)

        return Response("Poverty Data updated successfully")
