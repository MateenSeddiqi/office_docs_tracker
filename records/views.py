from django.shortcuts import render
from .models import IncomingDoc, OutgoingDoc
# Create your views here.


def incomingDoc(request):
    incomingDocs = IncomingDoc.objects.all()
    return render (request, 'records/incomingDocs.html', {
        'incomingDocs': incomingDocs,
        })

def outgoingDoc(request):
    outgoingDocs = IncomingDoc.objects.all()
    return render (request, 'records/outgoingDocs.html', {
        'outgoingDocs': outgoingDocs,
        })