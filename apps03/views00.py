from apps03.models import Guest, accomodation_category, accompacks,rentalunit,DueReceipt,Receipt,room_category
from django.shortcuts import render
from .forms import rentalunitForm,GuestForm, accom_categoryForm, accompacksForm,DueReceiptForm,ReceiptForm
from .forms import room_categoryForm
from django.http import HttpResponse
from django.contrib import messages



def   login(request):
      a = "Hello"
      print(a)

      
      template = loader.get_template('apps03/index.html')
      return HttpResponse(template.render())

def login0(request):
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
    print('Now in dashb view')
    st = rentalunit.objects.all() # Collect all records from table 
    count= rentalunit.objects.all().count()
    print(count)
   # return render(request,'display.html',{'st':st})
    return render (request,'apps03/viewpro.html', {
        'rental_units': st
    })


def task_create(request):
    if request.method == 'POST':
        form = RentalUnitForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = RentalUnitForm()
    return render(request,  'apps03/add_poll.html', {'form': form})
 
def add_guest(request):
     if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            print('valid')
     else:
            form = GuestForm()
     return render(request,  'apps03/add_guest.html', {'form': form})

def add_roomcat(request):
     if request.method == 'POST':
        form = room_categoryForm(request.POST)
        if form.is_valid():
            print('valid')
     else:
            form = room_categoryForm()
     return render(request, 'apps03/add_roomcat.html',{'form': form})


def add_accomcat(request):
     if request.method == 'POST':
        form = accom_categoryForm(request.POST)
        if form.is_valid():
            print('valid')
     else:
            form = accom_categoryForm()
     return render(request, 'apps03/add_accomcat.html',{'form': form})

def roomcatsv(request):
      if request.method=='POST':
         code0=request.POST['code']
         desc0=request.POST['desc']
         roomcat=room_category.objects.create(code=code0,desc=desc0)
       
         roomcat.save()
         messages.success(request,'Data has been submitted')
         form = room_categoryForm()
         return render(request, 'apps03/add_roomcat.html',{'form': form})


def commcatsv(request):
      if request.method=='POST':
         code0=request.POST['code']
         desc0=request.POST['desc']
         comcat=accomodation_category.objects.create(code=code0,desc=desc0)
       
         comcat.save()
         messages.success(request,'Data has been submitted')
         form = accom_categoryForm()
         return render(request, 'apps03/add_accomcat.html',{'form': form})


def add_rentalunit(request):
     if request.method == 'POST':
        form = rentalunitForm(request.POST)
        if form.is_valid():
            print('valid')
     else:
            form = rentalunitForm()
     return render(request, 'apps03/add_rentalunit.html',{'form': form})



def rentalunitpr(request):
    if request.method=='POST':
        roomno0=request.POST['roomno']
        roomdesc0=request.POST['roomdesc']
        roomtype0=request.POST['roomtype']
        rate0=request.POST['rate']
        rental=rentalunit.objects.create(roomno=roomno0,roomdesc=roomdesc0,roomtype=roomtype0, rate= rate0)
       
        rental.save()
        messages.success(request,'Data has been submitted')
        form = rentalunitForm()
    return render(request,  'apps03/add_rentalunit.html', {'form': form})

def addguest(request):
    if request.method=='POST':
        first_name0=request.POST['first_name']
        last_name0=request.POST['last_name']
        address0=request.POST['address']
        phone_number0=request.POST['phone_number'] 
        guestnumb0=request.POST['guestnumb']
        guest=Guest.objects.create(first_name=first_name0,last_name=last_name0,address=address0,phone_number=phone_number0,
                   guestnumb=   guestnumb0)
       
        guest.save()
        messages.success(request,'Data has been submitted')
        form = GuestForm()
    return render(request,  'apps03/add_guest.html', {'form': form})

def viewpro(request):
   # con = mysql.connector.connect(user='root', password='mysql2016', host='localhost', database='dbaccom0')
    cur = con.cursor()
    cur.execute("SELECT * FROM rentalunit")
    records=cur.fetchall()
    print(records)
    con.commit()
    cur.close()
    con.close()
    #context = {'viewpro' : user_order.objects.all()}
    return render(request, "apps03/viewpro.html", {'records':records})
