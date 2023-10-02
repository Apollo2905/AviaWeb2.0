from django.contrib import admin
from .models import Booking
from .models import Ticket
from .models import TicketFlight
from .models import BoardingPass
from .models import Flight
from .models import Airport
from .models import Aircraft
from .models import Seat

admin.site.register(Booking)
admin.site.register(Ticket)
admin.site.register(TicketFlight)
admin.site.register(BoardingPass)
admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Seat)
