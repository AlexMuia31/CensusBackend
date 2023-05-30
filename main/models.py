from django.db import models

# Create your models here.


class Census(models.Model):
    total_population = models.CharField(max_length=100)
    white_alone = models.CharField(max_length=100)
    black_or_african_american_alone = models.CharField(max_length=100)
    american_indian_and_alaskan_native_alone = models.CharField(max_length=100)
    asian_alone = models.CharField(max_length=100)
    native_hawaiian_and_other_pacific_islander_alone = models.CharField(
        max_length=100)
    other_race_alone = models.CharField(max_length=100)
    geo_id = models.CharField(max_length=100)


class Insurance(models.Model):
    age_category = models.CharField(max_length=100)
    people_insured = models.CharField(max_length=100)
    people_not_insured = models.CharField(max_length=100)


class Total(models.Model):
    total_population = models.CharField(max_length=100)
    white_alone = models.CharField(max_length=100)
    black_or_african_american_alone = models.CharField(max_length=100)
    american_indian_and_alaskan_native_alone = models.CharField(max_length=100)
    asian_alone = models.CharField(max_length=100)
    native_hawaiian_and_other_pacific_islander_alone = models.CharField(
        max_length=100)
    other_race_alone = models.CharField(max_length=100)
    two_or_more_races = models.CharField(max_length=100)
    other = models.CharField(max_length=100)
    median_household_income = models.CharField(max_length=100)
