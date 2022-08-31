from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



 
urlpatterns = [ 

    path('apps03/login/', views.login, name='login'),
    path('apps03/add_accomcat/', views.add_accomcat, name='add_accomcat'),
    
    

    path('dashboard/', views.dashboard, name='dashboard'),
    path('rentalunitpr/', views.rentalunitpr, name='rentalunitpr'),
    path('apps03/dashboard/', views.dashboard, name='dashboard'),
    path('apps03/polls_list/', views.polls_list, name='polls_list'),
    path('apps03/task_create/', views.task_create, name='task_create'),
    path('viewpro/', views.viewpro, name='viewpro'),



    path('commcatsv/', views.commcatsv, name='commcatsv'), 

    path('apps03/add_roomcat/', views.add_roomcat, name='add_roomcat'),
    path('roomcatsv/', views.roomcatsv, name='roomcatsv'), 


    path('apps03/add_rentalunit/', views.add_rentalunit, name='add_rentalunit'),
    path('apps03/add_guest/',views.add_guest, name='add_guest'),
    path('addguest/',views.addguest, name='addguest'),

       ]






