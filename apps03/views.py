
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from apps03.models import  bookings, chk
from apps03.forms import  bookingsForm,chkForm
from django.db import models, router, connections
import mysql.connector



def login(request):
    # 'NAME'    : 'dbapps03',                 # <-- UPDATED line 
     #   'USER'    : 'doadmin',                     # <-- UPDATED line
     #   'PASSWORD': 'AVNS_opSyNyIDAt49SbpzqG_',              # <-- UPDATED line
     #   'HOST'    : 'db-mysql-nyc3-16778-duser-11647348-0.b.db.ondigitalocean.com',                
    #    'PORT'    : '25060',
 
     
  con = mysql.createConnection({
  host: "db-mysql-nyc3-16778-duser-11647348-0.b.db.ondigitalocean.com",
  user: "doadmin",
  port: 25060,
  password: "AVNS_opSyNyIDAt49SbpzqG_",
  database: "dbapps03",
  ssl: {
    ca: fs.readFileSync(__dirname + '/public/ca-certificate.crt.txt'),
    rejectUnauthorized: false
    }
  });

 

  app.post('/', function (req, res) {con.connect(function (err) {
    if (err) throw err;
    con.end();
    res.send("Connected!");
    }});
     
          
    #  template = loader.get_template('apps03/mysqtemp.html')
     # return HttpResponse(template.render())
  ##  form = chkForm()
  ##  return render(request, 'apps03/add_checkins.html',{'form': form})





        
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
        form = chkForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
            form = chkForm()
    return render(request, 'apps03/add_checkins.html',{'form': form})








def checkinsaddpr(request):
    if request.method=='POST':
        seq0=request.POST['seq']
        rm0=request.POST['rm']
        occ0=request.POST['mark']
        days0=request.POST['days']
        rate0=request.POST['rate']
        checkins0=chk.objects.create(seq=seq0,rm=rm0,mark=occ0,days=days0, rate= rate0)      
        checkins0.save()  
  
        checkinss =chk.objects.all() # Collect all records from table   
        return render (request,'apps03/checkinslist.html', {
        'checkinss': checkinss
    })

 

def checkins_list(request):
     #rentalunit2.objects.all().delete()
     checkinss = chk.objects.all() # Collect all records from table 
    
    
  
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
   
    
    
    
    
    
    
    
