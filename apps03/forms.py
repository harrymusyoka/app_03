from django import forms
from apps03.models import   bookings

class checkinsForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = checki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
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
