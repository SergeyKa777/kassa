from django.contrib import admin
from .models import *


class Excursion_ext(admin.ModelAdmin):
    list_display = ('name', 'ticket_qty','time','ticket_price','discount_ticket_price')

class Tickets_ext(admin.ModelAdmin):
    list_display = ('excurs','date','normal_ticket','discount_ticket','free_ticket','cashier')


admin.site.register(Excursion,Excursion_ext)

admin.site.register(Tickets,Tickets_ext)

# Register your models here.
