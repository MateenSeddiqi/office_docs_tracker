from django.shortcuts import render
from .models import IncomingDoc, OutgoingDoc
# Create your views here.


def records(request):
    return render (request, 'records/records.html')