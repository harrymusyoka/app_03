from django.shortcuts import render


from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
 
from django.views.generic import UpdateView
from django.views.generic import CreateView
 


def   login(request):
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
