from django.urls import path
from . import views

app_name='records'

urlpatterns=[
    path('incomingDoc/', views.incomingDoc, name='incomingDoc'), 
    path('outgoingDoc/', views.outgoingDoc, name='outgoingDoc'),
]