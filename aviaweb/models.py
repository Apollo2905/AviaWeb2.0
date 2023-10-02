from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
import jsonfield


class Booking(models.Model):
    book_ref = models.CharField(primary_key=True, max_length=6)
    book_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'bookings'
        managed = False


class Ticket(models.Model):
    ticket_no = models.CharField(primary_key=True)
    book_ref = models.ForeignKey(Booking, on_delete=models.CASCADE, db_column='book_ref')
    passenger_id = models.CharField(max_length=20)
    contact_data = jsonfield.JSONField()

    class Meta:
        db_table = 'tickets'
        managed = False


class TicketFlight(models.Model):
    ticket_no = models.OneToOneField(Ticket, on_delete=models.CASCADE, db_column='ticket_no', primary_key=True)
    flight_id = models.ForeignKey('aviaweb.Flight', on_delete=models.CASCADE, db_column='flight_id')
    fare_conditions = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'ticket_flights'
        managed = False


class BoardingPass(models.Model):
    ticket_no = models.OneToOneField(Ticket, on_delete=models.CASCADE, db_column='ticket_no', primary_key=True)
    flight_id = models.OneToOneField('aviaweb.TicketFlight', on_delete=models.CASCADE, db_column='flight_id')
    boarding_no = models.IntegerField()
    seat_no = models.CharField(max_length=4)

    class Meta:
        db_table = 'boarding_passes'
        managed = False


class Flight(models.Model):
    flight_id = models.CharField(primary_key=True)
    flight_no = models.CharField(max_length=6)
    scheduled_departure = models.DateTimeField()
    scheduled_arrival = models.DateTimeField()
    departure_airport = models.ForeignKey('aviaweb.Airport', on_delete=models.CASCADE, related_name='departure',
                                          db_column='departure_airport')
    arrival_airport = models.ForeignKey('aviaweb.Airport', on_delete=models.CASCADE, related_name='arrival',
                                        db_column='arrival_airport')
    status = models.CharField(max_length=20)
    aircraft_code = models.ForeignKey('aviaweb.Aircraft', on_delete=models.CASCADE, db_column='aircraft_code')
    actual_departure = models.DateTimeField()
    actual_arrival = models.DateTimeField()

    class Meta:
        db_table = 'flights'
        managed = False


class Airport(models.Model):
    airport_code = models.CharField(primary_key=True)
    airport_name = models.TextField()
    city = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    timezone = models.TextField()

    class Meta:
        db_table = 'airports'
        managed = False


class Aircraft(models.Model):
    aircraft_code = models.CharField(primary_key=True, max_length=3)
    model = models.TextField()
    range = models.IntegerField()

    class Meta:
        db_table = 'aircrafts'
        managed = False


class Seat(models.Model):
    aircraft_code = models.ForeignKey('aviaweb.Aircraft', on_delete=models.CASCADE, db_column='aircraft_code')
    seat_no = models.CharField(primary_key=True)
    fare_conditions = models.CharField(max_length=10)

    class Meta:
        db_table = 'seats'
        managed = False
