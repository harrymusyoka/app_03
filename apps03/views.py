from django.shortcuts import render


from django.shortcuts import render

from django.http import HttpResponse
from django.contrib import messages



def login(request):
      a = "Hello"
      print(a)
      HttpResponse('apps03/index.html')
