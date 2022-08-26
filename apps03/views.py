from django.shortcuts import render


from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from apps03.models import Guest, accomodation_category
from apps03.models import accompacks,rentalunit,DueReceipt,Receipt,room_category
from .forms import rentalunitForm,GuestForm, accom_categoryForm
from .forms import accompacksForm,DueReceiptForm,ReceiptForm
from .forms import room_categoryForm
import win32api

def login(request):
      a = "Hello"
      print(a)

      
      template = loader.get_template('apps03/index.html')
      return HttpResponse(template.render())
      
      
def login1(request):
    win32api.MessageBox(0, 'hello', 'harry')
    if request.method == 'POST':
        form = rentalunitForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = rentalunitForm()
    return render(request,  'apps03/main-menu.html', {'form': form})
