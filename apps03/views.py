from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages

from .forms import rentalunitForm, rentalunitvForm

from .models import rentalunit
import mysql.connector

def   login(request):


      #mydb = mysql.connector.connect(
      #host="db-mysql-nyc3-16778-do-user-11647348-0.b.db.ondigitalocean.com",
      #user="doadmin",
      #password="AVNS_opSyNyIDAt49SbpzqG_",
      #database="defaultdb")

      #mycursor = mydb.cursor()

      #sql = "DROP TABLE rentalunit"

      #mycursor.execute(sql) 
      a = "Hello"
      print(a)

      
      template = loader.get_template('apps03/main-menu.html')
      return HttpResponse(template.render())
      
def polls_list(request):
      HttpResponse('apps03/poll_list.html')

def ru_list(request):
     #rentalunit2.objects.all().delete()
     rental_units = rentalunit.objects.all() # Collect all records from table 
    
    
  
     return render (request,'apps03/rentalunitslist.html', {
        'rental_units': rental_units
    })


 
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


def view_rentalunit(request):
     if request.method == 'POST':
        form = rentalunitvForm(request.POST)
        if form.is_valid():
            print('valid')
     else:
            form = rentalunitvForm()
     return render(request, 'apps03/view_rentalunit.html',{'rental_units': form})


def edit_rentalunit(request, rn):
         
     if request.method == 'POST':
        form = rentalunitForm(request.POST)
        if form.is_valid():
            print('valid')
     else:
            form = rentalunitForm()
     return render(request, 'apps03/edit_rentalunit.html',{'form': form})






def addguest(request):
       template = loader.get_template('apps03/main-menu.html')
       return HttpResponse(template.render())

def viewpro(request):
     template = loader.get_template('apps03/main-menu.html')
     return HttpResponse(template.render())


def rentalunitpr(request):
    if request.method=='POST':
 
        roomno0=request.POST['roomno']
        roomdesc0=request.POST['roomdesc']
        roomtype0=request.POST['roomtype']
        rate0=request.POST['rate']
        
        rental=rentalunit.objects.create(roomno=roomno0,roomdesc=roomdesc0,roomtype=roomtype0, rate= rate0)
       
        rental.save()
       # messages.success(request,'Data has been submitted')
      #  form = rentalunitForm()
   # return render(request,  'apps03/add_rentalunit.html', {'form': form})
        rental_units = rentalunit.objects.all() # Collect all records from table 
    
    
  
        return render (request,'apps03/rentalunitslist.html', {
        'rental_units': rental_units
          })










