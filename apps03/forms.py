from django import forms
from .models import  Checkinstab

class checkinsForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = checkinstab
        fields = ['seq', 'rm', 'occ', 'days', 'rate' ]

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }
