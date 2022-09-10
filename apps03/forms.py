from django import forms
from apps03.models import   bookings


        
       
class bookingsForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = bookings
        fields = ['seq', 'rm', 'mark', 'days', 'rate' ]

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }
