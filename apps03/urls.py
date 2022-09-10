from django.urls import path 
 
from . import views


urlpatterns = [
    path('apps03/year_archive/', views.year_archive),
    path('apps03/login/', views.login),
    path('apps03/checkins_list/', views.checkins_list),
    path('apps03/checkinsadd/', views.checkinsadd, name='checkinsadd'),
    path('apps03/view_booking/', views.view_booking),
    path('apps03/checkinsaddpr/', views.checkinsaddpr, name='checkinsaddpr'),

    
]
 
