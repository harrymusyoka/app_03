from django.shortcuts import render


from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.db import models
from django.views.generic import UpdateView
from django.views.generic import CreateView
 






def   login(request):
      a = "Hello"
      print(a)

      
      template = loader.get_template('apps03/main-menu.html')
      return HttpResponse(template.render())
      
      
def login1(request):
   
    if request.method == 'POST':
        form = rentalunitForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = rentalunitForm()
    return render(request,  'apps03/main-menu.html', {'form': form})
    
    
    

  

def polls_list(request):
      HttpResponse('apps03/poll_list.html')



def dashboard(request):
      template = loader.get_template('apps03/main-menu.html')
      return HttpResponse(template.render())


def task_create(request):
      template = loader.get_template('apps03/main-menu.html')
      return HttpResponse(template.render())

def add_guest(request):
      template = loader.get_template('apps03/main-menu.html')
      return HttpResponse(template.render())

def add_roomcat(request):
       template = loader.get_template('apps03/main-menu.html')
       return HttpResponse(template.render())


def add_accomcat(request):
       template = loader.get_template('apps03/main-menu.html')
       return HttpResponse(template.render())

def roomcatsv(request):
       template = loader.get_template('apps03/main-menu.html')
       return HttpResponse(template.render())


def commcatsv(request):
       template = loader.get_template('apps03/main-menu.html')
       return HttpResponse(template.render())


def add_rentalunit(request):
       template = loader.get_template('apps03/main-menu.html')
       return HttpResponse(template.render())



def rentalunitpr(request):
       template = loader.get_template('apps03/main-menu.html')
       return HttpResponse(template.render())

def addguest(request):
       template = loader.get_template('apps03/main-menu.html')
       return HttpResponse(template.render())

def viewpro(request):
     template = loader.get_template('apps03/main-menu.html')
     return HttpResponse(template.render())












