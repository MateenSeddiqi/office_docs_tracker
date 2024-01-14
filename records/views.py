from django.shortcuts import render
from .models import IncomingDoc, OutgoingDoc
from .forms import IncomingDocForm
# Create your views here.

def records(request):
    return render (request, 'records/records.html')
    

# code of incoming docs to display incoming files
def incomingDoc(request):  
    incomingDocs = IncomingDoc.objects.all()
    return render (request, 'records/incomingDocs.html', {
        'incomingDocs': incomingDocs,
        })


def addIncomingDoc(request):
    # if request.method == 'POST':
    incomingDocForm = IncomingDocForm()
    return render (request, 'records/incomingDocForm.html', {
        'incomingDocForm': incomingDocForm
    }) 



# code of outgoing docs to display outgoing files
def outgoingDoc(request):
    outgoingDocs = IncomingDoc.objects.all()
    return render (request, 'records/outgoingDocs.html', {
        'outgoingDocs': outgoingDocs,
        })