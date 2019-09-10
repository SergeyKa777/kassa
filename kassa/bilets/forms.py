from django.forms import Form,ModelForm
from .models import *

class Tick(ModelForm):
    class Meta:
        model=Tickets
        fields=['excurs','normal_ticket','discount_ticket','free_ticket','cashier']
