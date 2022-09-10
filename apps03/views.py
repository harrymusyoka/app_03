
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from .forms import checkinsForm
from .models import Checki, bookings
from .models import Article, bookingsForm


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
      template = loader.get_template('apps03/checkinslist.html')
      return HttpResponse(template.render())

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'apps03/year_archive.html', context)



def checkinsadd(request):
    if request.method=='POST':
        seq0=request.POST['seq']
        rm0=request.POST['rm']
        occ0=request.POST['occ']
        days0=request.POST['days']
        rate0=request.POST['rate']
        checkins0=bookings.objects.create(seq=seq0,rm=rm0,occ=occ0,days=days0, rate= rate0)      
        checkins0.save()
        messages.success(request,'Data has been submitted')
        form = checkinsForm()
    return render(request,  'apps03/add_checkins.html', {'form': form})

def checkins_list(request):
     #rentalunit2.objects.all().delete()
     checkinss = bookings.objects.all() # Collect all records from table 
    
    
  
     return render (request,'apps03/checkinslist.html', {
        'checkinss': checkinss
    })
