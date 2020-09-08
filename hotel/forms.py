from django import forms
import datetime
#from .models import ROOM_CATEGORIES

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES=(
        ('YAC','AC'), # (CODE , Display)
        ('NAC','NON-AC'),
        ('DEL','DELUXE'),
        ('KIN','KING'),
        ('QUE','QUEEN'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H%M",] )
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H%M",] )

