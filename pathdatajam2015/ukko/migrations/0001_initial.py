# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinalData',
            fields=[
                ('station', models.CharField(max_length=200, blank=True)),
                ('entry', models.BigIntegerField(null=True, blank=True)),
                ('exit', models.BigIntegerField(null=True, blank=True)),
                ('est', models.DateField(null=True, blank=True)),
                ('events', models.CharField(max_length=200, blank=True)),
                ('precipitation_in', models.CharField(max_length=200, blank=True)),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'final_data',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TurnstileSan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rownum', models.BigIntegerField(null=True, blank=True)),
                ('entry', models.IntegerField(null=True, blank=True)),
                ('exit', models.IntegerField(null=True, blank=True)),
                ('station', models.CharField(max_length=200, blank=True)),
                ('date_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'turnstile_san',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('est', models.DateField(null=True, blank=True)),
                ('max_temperature_f', models.IntegerField(null=True, blank=True)),
                ('mean_temperature_f', models.IntegerField(null=True, blank=True)),
                ('min_temperature_f', models.IntegerField(null=True, blank=True)),
                ('max_dew_point_f', models.IntegerField(null=True, blank=True)),
                ('mean_dew_point_f', models.IntegerField(null=True, blank=True)),
                ('min_dewpoint_f', models.IntegerField(null=True, blank=True)),
                ('max_humidity', models.IntegerField(null=True, blank=True)),
                ('mean_humidity', models.IntegerField(null=True, blank=True)),
                ('min_humidity', models.IntegerField(null=True, blank=True)),
                ('max_sea_level_pressure_in', models.FloatField(null=True, blank=True)),
                ('mean_sea_level_pressure_in', models.FloatField(null=True, blank=True)),
                ('min_sea_level_pressure_in', models.FloatField(null=True, blank=True)),
                ('max_visibility_miles', models.IntegerField(null=True, blank=True)),
                ('mean_visibility_miles', models.IntegerField(null=True, blank=True)),
                ('min_visibility_miles', models.IntegerField(null=True, blank=True)),
                ('max_wind_speed_mph', models.IntegerField(null=True, blank=True)),
                ('mean_wind_speed_mph', models.IntegerField(null=True, blank=True)),
                ('max_gust_speed_mph', models.IntegerField(null=True, blank=True)),
                ('precipitation_in', models.CharField(max_length=200, blank=True)),
                ('cloud_cover', models.IntegerField(null=True, blank=True)),
                ('events', models.CharField(max_length=200, blank=True)),
                ('wind_dir_degrees', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'weather_data',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
