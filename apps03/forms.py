from django import forms
from .models import  Guest, accomodation_category, accompacks,accomodation_category,rentalunit,DueReceipt,room_category



class rentalunitForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = rentalunit
        fields = ['roomno', 'roomdesc', 'roomtype', 'rate' ]

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }


class rentalunitvForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = rentalunit
        fields = ['roomno', 'roomdesc', 'roomtype', 'rate']

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }




class GuestForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = Guest
        fields = fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }
 
class room_categoryForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = room_category
        fields = ['code', 'desc' ]
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }

class accom_categoryForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = accomodation_category
        fields = ['code', 'desc' ]
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 20}),
        }

class accompacksForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = accompacks
        fields = fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }

class DueReceiptForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = DueReceipt
        fields = fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }




