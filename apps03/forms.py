from django import forms
from .models import  checkins



class checkinsForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = checkins
        fields = ['seq', 'rm', 'occ', 'days', 'rate' ]

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }
