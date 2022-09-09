
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages



from .models import Article


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

      
      template = loader.get_template('apps03/index.html')
      return HttpResponse(template.render())

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'apps03/year_archive.html', context)

