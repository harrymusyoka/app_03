from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



 
urlpatterns = [ 

    path('apps03/login/', views.login, name='login'),
       ]






