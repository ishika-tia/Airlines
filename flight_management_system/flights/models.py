from django.db import models

# Create your models here.

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

    def __str__(self):
        return f'{self.airline_name}'

class Passenger(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=30, blank=True, null=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING, blank=True, null=True)
    checked_in = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passenger'