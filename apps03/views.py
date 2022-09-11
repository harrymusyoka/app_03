
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from apps03.models import  bookings
from apps03.forms import  bookingsForm
import mysql.connector



def login(request):
     
    #  template = loader.get_template('apps03/mysqtemp.html')
     # return HttpResponse(template.render())
    form = bookingsForm()
    return render(request, 'apps03/add_checkins.html',{'form': form})





def login4(request):
    myresult = "Harry Musyoka"
    mydb = mysql.connector.connect(
    host="db-mysql-nyc3-16778-do-user-11647348-0.b.db.ondigitalocean.com",
    user="doadmin",
    password="AVNS_opSyNyIDAt49SbpzqG_",
    database="dbapps03b"
    )
    mycursor = mydb.cursor()
 
    mycursor.execute("SELECT table_name FROM information_schema.tables;")
 
    myresult = mycursor.fetchall()

    return render (request,'apps03/dispmsg.html', {
       'messages': myresult
       })



def login3(request):
    mydb = mysql.connector.connect(
    host="db-mysql-nyc3-16778-do-user-11647348-0.b.db.ondigitalocean.com",
    user="doadmin",
    password="AVNS_opSyNyIDAt49SbpzqG_",
    database="dbapps03b"
    )
    mycursor = mydb.cursor()
 
    mycursor.execute("Show tables;")
 
    myresult = mycursor.fetchall()
 
    #for x in myresult:
     #   print(x)

    return render (request,'apps03/checkinslist.html', {
       'checkinss': myresult
       })


        
def    mysqlfunc(request):
       x="43"
       print(x)

def   login1(request):
      #mydb = mysql.connector.connect(
      #host="db-mysql-nyc3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-16778-do-user-11647348-0.b.db.ondigitalocean.com",
      #user="doadmin",
      #password="AVNS_opSyNyIDAt49SbpzqG_",
      #database="defaultdb")
      #mycursor = mydb.cursor()
      #sql = "DROP TABLE rentalunit"
      #mycursor.execute(sql) 
      a = "Hello"
     
     # checkinss = bookings.objects.all() # Collect all records from table 
     
    
     # count = bookings.objects.all().count()
   #   print(count)
   #   return render (request,'apps03/checkinslist.html', {
    #    'checkinss': checkinss
  #    })

     
def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'apps03/year_archive.html', context)

def checkinsadd(request):
    if request.method == 'POST':
        form = checkiForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
            form = checkiForm()
    return render(request, 'apps03/add_checkins.html',{'form': form})








def checkinsaddpr(request):
    if request.method=='POST':
        seq0=request.POST['seq']
        rm0=request.POST['rm']
        occ0=request.POST['mark']
        days0=request.POST['days']
        rate0=request.POST['rate']
        checkins0=checki.objects.create(seq=seq0,rm=rm0,mark=occ0,days=days0, rate= rate0)      
        checkins0.save()        
        checkinss = checki.objects.all() # Collect all records from table   
        return render (request,'apps03/checkinslist.html', {
        'checkinss': checkinss
    })

 

def checkins_list(request):
     #rentalunit2.objects.all().delete()
     checkinss = bookings.objects.all() # Collect all records from table 
    
    
  
     return render (request,'apps03/checkinslist.html', {
        'checkinss': checkinss
    })
    
    
def view_booking(request):
     if request.method == 'POST':
        form = bookingsForm(request.POST)
        if form.is_valid():
            print('valid')
     else:
            form = bookingsForm()
     return render(request, 'apps03/view_bookings.html',{'bookings': form})
   
    
    
    
    
    
    
    
