from django.urls import path
from . import views

app_name='records'

urlpatterns=[
    path('', views.records, name='records'),
    path('incomingDoc/', views.incomingDoc, name='incomingDoc'), 
    path('outgoingDoc/', views.outgoingDoc, name='outgoingDoc'),
    path('addIncomingDoc/', views.addIncomingDoc, name='addIncomingDoc'),
]