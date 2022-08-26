from django.shortcuts import render


from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from .forms import rentalunitForm
from django.views.generic import UpdateView
from apps03.models import rentalunit
from apps03.forms import rentalunitForm

class login(UpdateView):
      model = rentalunit
      form_class = rentalunitForm
      template_name = 'apps03/index2.html'

class login3(UpdateView):
      model = rentalunit
      form_class = rentalunitForm
      template_name = 'apps03/main-menu.html'

def   login0(request):
      a = "Hello"
      print(a)

      
      template = loader.get_template('apps03/index.html')
      return HttpResponse(template.render())
      
      
def login1(request):
   
    if request.method == 'POST':
        form = rentalunitForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = rentalunitForm()
    return render(request,  'apps03/main-menu.html', {'form': form})
