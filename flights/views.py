from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flight, Passenger
from .forms import FlightForm, PassengerForm


# Create your views here.
def home(request):
    return render(request, 'flights/home.html')

def index(request):
    return render(request, 'flights/index.html', {
        'flights': Flight.objects.all()
    })

def passenger(request):
    return render(request, 'flights/passenger.html', {
        'passengers': Passenger.objects.all()
    })

def view_flight(request, id):
    flight = Flight.objects.get(pk = id)
    return HttpResponseRedirect(reverse('index'))

def view_passenger(request, id):
    passenger = Passenger.objects.get(pk = id)
    return HttpResponseRedirect(reverse('passenger'))

def add(request):
    if request.method == 'POST':
        form =  FlightForm(request.POST)
        if form.is_valid():
            new_flight_id = form.cleaned_data['flight_id']
            new_airline_name = form.cleaned_data['airline_name']
            new_dep_time = form.cleaned_data['dep_time']
            new_arr_time = form.cleaned_data['arr_time']
            new_service = form.cleaned_data['service']
            new_aircraft_id = form.cleaned_data['aircraft_id']
            new_route_no = form.cleaned_data['route_no']

            new_flight = Flight(
            flight_id = new_flight_id,
            airline_name = new_airline_name,
            dep_time = new_dep_time,
            arr_time = new_arr_time,
            service = new_service,
            aircraft_id = new_aircraft_id,
            route_no = new_route_no
            )
            new_flight.save()
            return render(request, 'flights/add.html',{
                'form' : FlightForm(),
                'success': True
            })
    else:
        form = FlightForm()
    return render(request, 'flights/add.html', {
        'form' : FlightForm()
    })

def addp(request):
    if request.method == 'POST':
        form =  PassengerForm(request.POST)
        if form.is_valid():
            new_p_id: form.cleaned_data['p_id']
            new_p_name: form.cleaned_data['p_name']
            new_flight: form.cleaned_data['flight']
            new_checked_in: form.cleaned_data['checked_in']

            new_passenger = Passenger(
            p_id = new_p_id,
            p_name = new_p_name,
            flight = new_flight,
            checked_in = new_checked_in
            )
            new_passenger.save()
            return render(request, 'flights/addp.html',{
                'form' : PassengerForm(),
                'success': True
            })
    else:
        form = PassengerForm()
    return render(request, 'flights/addp.html', {
        'form' : PassengerForm()
    })