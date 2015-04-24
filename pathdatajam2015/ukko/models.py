# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class FinalData(models.Model):
    station = models.CharField(max_length=-1, blank=True)
    entry = models.BigIntegerField(blank=True, null=True)
    exit = models.BigIntegerField(blank=True, null=True)
    est = models.DateField(blank=True, null=True)
    events = models.CharField(max_length=-1, blank=True)
    precipitation_in = models.CharField(max_length=-1, blank=True)
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'final_data'


class TurnstileSan(models.Model):
    rownum = models.BigIntegerField(blank=True, null=True)
    entry = models.IntegerField(blank=True, null=True)
    exit = models.IntegerField(blank=True, null=True)
    station = models.CharField(max_length=-1, blank=True)
    date_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turnstile_san'

class WeatherData(models.Model):
    est = models.DateField(blank=True, null=True)
    max_temperature_f = models.IntegerField(blank=True, null=True)
    mean_temperature_f = models.IntegerField(blank=True, null=True)
    min_temperature_f = models.IntegerField(blank=True, null=True)
    max_dew_point_f = models.IntegerField(blank=True, null=True)
    mean_dew_point_f = models.IntegerField(blank=True, null=True)
    min_dewpoint_f = models.IntegerField(blank=True, null=True)
    max_humidity = models.IntegerField(blank=True, null=True)
    mean_humidity = models.IntegerField(blank=True, null=True)
    min_humidity = models.IntegerField(blank=True, null=True)
    max_sea_level_pressure_in = models.FloatField(blank=True, null=True)
    mean_sea_level_pressure_in = models.FloatField(blank=True, null=True)
    min_sea_level_pressure_in = models.FloatField(blank=True, null=True)
    max_visibility_miles = models.IntegerField(blank=True, null=True)
    mean_visibility_miles = models.IntegerField(blank=True, null=True)
    min_visibility_miles = models.IntegerField(blank=True, null=True)
    max_wind_speed_mph = models.IntegerField(blank=True, null=True)
    mean_wind_speed_mph = models.IntegerField(blank=True, null=True)
    max_gust_speed_mph = models.IntegerField(blank=True, null=True)
    precipitation_in = models.CharField(max_length=-1, blank=True)
    cloud_cover = models.IntegerField(blank=True, null=True)
    events = models.CharField(max_length=-1, blank=True)
    wind_dir_degrees = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_data'
