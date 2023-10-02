from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *  # импортирование модели

from datetime import datetime


def home(request):
    departure = request.GET.get('departure')
    arrival = request.GET.get('arrival')
    scheduled_departure = request.GET.get('scheduled_departure')
    search = request.GET.get('search')
    # scheduled_arrival = request.GET.get('scheduled_arrival')

    if departure or arrival or scheduled_departure:
        flights_array = Flight.objects.filter(
            Q(departure_airport__city__icontains=departure) &
            Q(arrival_airport__city__icontains=arrival) &
            Q(scheduled_departure__date__icontains=scheduled_departure)
            # Q(scheduled_arrival__date__icontains=arrival)
        )

        return render(request, 'flights.html', {'flights': flights_array})
    return render(request, 'home.html', {})


def bookings(request):
    pass
