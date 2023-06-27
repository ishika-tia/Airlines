# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Flight(models.Model):
    flight_id = models.IntegerField(primary_key=True)
    airline_name = models.CharField(max_length=20, blank=True, null=True)
    dep_time = models.CharField(max_length=5, blank=True, null=True)
    arr_time = models.CharField(max_length=5, blank=True, null=True)
    service = models.CharField(max_length=20, blank=True, null=True)
    aircraft_id = models.IntegerField(blank=True, null=True)
    route_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flight'


class Passenger(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=30, blank=True, null=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING, blank=True, null=True)
    checked_in = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passenger'
