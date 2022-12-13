from django import forms
from .models import Flight, Passenger

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_id',
            'airline_name',
            'dep_time',
            'arr_time',
            'service',
            'aircraft_id',
            'route_no']
        labels = {
            'flight_id': 'Flight ID',
            'airline_name': 'Airline Name',
            'dep_time': 'Departure Time',
            'arr_time': 'Arrival Time',
            'service': 'Service',
            'aircraft_id': 'Aircraft ID',
            'route_no': 'Route No.'
        }
        widgets ={
            'flight_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'airline_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dep_time': forms.TimeInput(format='%H:%M'),
            'arr_time': forms.TimeInput(format='%H:%M'),
            'service': forms.TextInput(attrs={'class': 'form-control'}),
            'aircraft_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'route_no': forms.NumberInput(attrs={'class': 'form-control'})
        }

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['p_id',
            'p_name',
            'flight',
            'checked_in'
            ]
        labels = {
            'p_id': 'Passenger ID',
            'p_name': 'Passenger Name',
            'flight': 'Flight',
            'checked_in': 'Check-In Status'
        }
        widgets ={
            'p_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'p_name': forms.TextInput(attrs={'class': 'form-control'}),
            'flight': forms.TextInput(attrs={'class': 'form-control'}),
            'checked_in': forms.TextInput(attrs={'class': 'form-control'})
        }