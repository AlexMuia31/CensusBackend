from django.db import models

# Create your models here.

choices = (
    ('M', 'male'),
    ('F', 'female')
)


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

    def __str__(self):
        return self.total_population


class PopulationBySex(models.Model):
    total_population = models.CharField(max_length=100)
    under_5_years = models.CharField(max_length=100)
    five_to_9_years = models.CharField(max_length=100)
    ten_to_14_years = models.CharField(max_length=100)
    fifteen_to_17_years = models.CharField(max_length=100)
    eighteen_to_19_years = models.CharField(max_length=100)
    Twenty_years = models.CharField(max_length=100)
    Twenty_one_years = models.CharField(max_length=100)
    Twenty_two_to_24 = models.CharField(max_length=100)
    Twenty_Five_to_29 = models.CharField(max_length=100)
    Thirty_to_34_years = models.CharField(max_length=100)
    Thirty_Five_to_39 = models.CharField(max_length=100)
    Forty_to_44_years = models.CharField(max_length=100)
    Forty_Five_to_49 = models.CharField(max_length=100)
    Fifty_to_54_years = models.CharField(max_length=100)
    Fifty_five_to_59 = models.CharField(max_length=100)
    sixty_to_61_years = models.CharField(max_length=100)
    sixty_two_to_64 = models.CharField(max_length=100)
    sixty_five_to_66 = models.CharField(max_length=100)
    sixty_seven_to_69 = models.CharField(max_length=100)
    seventy_to_74_years = models.CharField(max_length=100)
    seventy_five_to_79 = models.CharField(max_length=100)
    Eighty_to_84_years = models.CharField(max_length=100)
    Eighty_five_and_above = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=2, choices=choices, null=True, blank=True)


class Poverty(models.Model):
    all_ages_in_poverty = models.CharField(max_length=100)
    ages_5_to_17_in_poverty = models.CharField(max_length=100)
    ages_0_17_in_poverty = models.CharField(max_length=100)


class MedianIncome(models.Model):
    Median_Income = models.CharField(max_length=100)
    White_Alone = models.CharField(max_length=100)
    Black_or_African_American = models.CharField(max_length=100)
    American_Indian_and_Alaska_Native_Alone = models.CharField(max_length=100)
    Asian_Alone = models.CharField(max_length=100)
    Two_or_more_races = models.CharField(max_length=100)
    Some_other_race_alone = models.CharField(max_length=100)
    Hispanic_or_Latino = models.CharField(max_length=100)