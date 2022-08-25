from django.shortcuts import render


from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages



def login(request):
      a = "Hello"
      print(a)

      
      template = loader.get_template('index.html')
      return HttpResponse(template.render())
