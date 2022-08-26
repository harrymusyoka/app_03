from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



 
urlpatterns = [ 

    path('aps03/login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('rentalunitpr/', views.rentalunitpr, name='rentalunitpr'),
    path('aps03/dashboard/', views.dashboard, name='dashboard'),
    path('aps03/polls_list/', views.polls_list, name='polls_list'),
    path('aps03/task_create/', views.task_create, name='task_create'),
    path('viewpro/', views.viewpro, name='viewpro'),


    path('aps03/add_accomcat/', views.add_accomcat, name='add_accomcat'),
    path('commcatsv/', views.commcatsv, name='commcatsv'), 

    path('aps03/add_roomcat/', views.add_roomcat, name='add_roomcat'),
    path('roomcatsv/', views.roomcatsv, name='roomcatsv'), 


    path('apaccom0/add_rentalunit/', views.add_rentalunit, name='add_rentalunit'),
    path('apaccom0/add_guest/',views.add_guest, name='add_guest'),
    path('addguest/',views.addguest, name='addguest'),
   ]






