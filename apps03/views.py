from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages

from .forms import rentalunitForm




def   login(request):
      a = "Hello"
      print(a)

      
      template = loader.get_template('apps03/main-menu.html')
      return HttpResponse(template.render())
      
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
     if request.method == 'POST':
        form = rentalunitForm(request.POST)
        if form.is_valid():
            print('valid')
     else:
            form = rentalunitForm()
     return render(request, 'apps03/add_rentalunit.html',{'form': form})




def rentalunitpr(request):
       template = loader.get_template('apps03/main-menu.html')
       return HttpResponse(template.render())

def addguest(request):
       template = loader.get_template('apps03/main-menu.html')
       return HttpResponse(template.render())

def viewpro(request):
     template = loader.get_template('apps03/main-menu.html')
     return HttpResponse(template.render())












