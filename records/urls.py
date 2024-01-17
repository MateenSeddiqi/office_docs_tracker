from django.urls import path
from . import views

app_name='records'

urlpatterns=[
    path('', views.records, name='records'),
    path('incomingDoc/', views.incomingDoc, name='incomingDoc'), 
    path('outgoingDoc/', views.outgoingDoc, name='outgoingDoc'),
    path('addIncomingDoc/', views.addIncomingDoc, name='addIncomingDoc'),
    path('addOutgoingDoc/', views.addOutgoingDoc, name='addOutgoingDoc'),
    path('IncomingDocDetails/<int:pk>', views.IncomingDocDetails, name='IncomingDocDetails'),
]