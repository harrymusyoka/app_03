from django import forms
from .models import  checki, bookings

class checkinsForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = checki
        fields = ['seq', 'rm', 'occ', 'days', 'rate' ]

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }
        
       
class bookingsForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = bookings
        fields = ['seq', 'rm', 'occ', 'days', 'rate' ]

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }
