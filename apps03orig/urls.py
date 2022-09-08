from django.urls import path
from books.views import RecordInterestView

urlpatterns = [
    #...
    path('author/<int:pk>/interest/', RecordInterestView.as_view(), name='author-interest'),
]
