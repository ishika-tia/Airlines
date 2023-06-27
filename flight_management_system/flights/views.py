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

def pindex(request):
    return render(request, 'flights/pindex.html', {
        'passengers': Passenger.objects.all()
    })

def view_flight(request, id):
    flight = Flight.objects.get(pk = id)
    return HttpResponseRedirect(reverse('index'))

def view_passenger(request, id):
    passenger = Passenger.objects.get(pk = id)
    return HttpResponseRedirect(reverse('pindex'))

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
        form = PassengerForm(request.POST)
        if form.is_valid():
            new_p_id = form.cleaned_data['p_id']
            new_p_name = form.cleaned_data['p_name']
            new_flight = form.cleaned_data['flight']
            new_checked_in = form.cleaned_data['checked_in']

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

def edit(request, id):
    if request.method == 'POST':
        flight = Flight.objects.get(pk=id)
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return render(request, 'flights/edit.html', {
                'form': form,
                'success': True
            })
    else:
        flight = Flight.objects.get(pk=id)
        form = FlightForm(instance=flight)
    return render(request, 'flights/edit.html', {
        'form': form
    })

def editp(request, id):
    if request.method == 'POST':
        passenger = Passenger.objects.get(pk=id)
        form = PassengerForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            return render(request, 'flights/editp.html', {
                'form': form,
                'success': True
            })
    else:
        passenger = Passenger.objects.get(pk=id)
        form = PassengerForm(instance=passenger)
    return render(request, 'flights/editp.html', {
        'form': form
    })
    
def delete(request, id):
  if request.method == 'POST':
    flight = Flight.objects.get(pk=id)
    flight.delete()
  return HttpResponseRedirect(reverse('index'))

def deletep(request, id):
  if request.method == 'POST':
   passenger = Passenger.objects.get(pk=id)
   passenger.delete()
  return HttpResponseRedirect(reverse('pindex'))