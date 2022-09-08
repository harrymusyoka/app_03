from django.urls import path

from . import views

urlpatterns = [
    path('apps03/<int:year>/', views.year_archive),
    path('apps03/<int:year>/<int:month>/', views.month_archive),
    path('apps03/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]

