from django import forms
from .models import  Guest, accomodation_category, accompacks,accomodation_category,rentalunit,DueReceipt,Receipt,room_category


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)




class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'email', 'job_title', 'bio')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))



class rentalunitForm(forms.ModelForm):
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

class ReceiptForm(forms.ModelForm):
    error_css_class='error-field'

    class Meta:
        model = Receipt
        fields = fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }



