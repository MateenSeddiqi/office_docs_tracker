from django.shortcuts import render, redirect
from .models import IncomingDoc, OutgoingDoc
from .forms import IncomingDocForm, OutgoingDocForm
from django.contrib import messages


# Create your views here.

def records(request):
    return render (request, 'records/records.html')
    

# code of incoming docs to display incoming files
def incomingDoc(request):  
    incomingDocs = IncomingDoc.objects.all()
    print(incomingDocs)
    return render (request, 'records/incomingDocs.html', {
        'incomingDocs': incomingDocs,
        })


def addIncomingDoc(request):
    incoming_doc_form = IncomingDocForm()
    if request.method == 'POST':
        incoming_doc_form = IncomingDocForm(request.POST, request.FILES)
        if incoming_doc_form.is_valid():
            newdoc = incoming_doc_form.save()
            return redirect('records:incomingDoc')  #pk=newdoc.id
            messages.success(request, 'Added')
        else:
            messages.error(request, 'Not  Added')
            
    context ={'incomingDocForm': incoming_doc_form} 
    return render(request, 'records/incomingDocForm.html', context)   

def IncomingDocDetails(request, pk):
    incomingDetails= IncomingDoc.objects.filter(id=pk)
    context = {
        'incomingDetails':incomingDetails,
    }
    return render(request, 'records/incomingDocDetails.html', context)


# code of outgoing docs to display outgoing files
def outgoingDoc(request):
    outgoingDocs = IncomingDoc.objects.all()
    return render (request, 'records/outgoingDocs.html', {
        'outgoingDocs': outgoingDocs,
        })


def addOutgoingDoc(request):
    outgoing_doc_form = OutgoingDocForm()
    if request.method == 'POST':
        outgoing_doc_form = OutgoingDocForm(request.POST, request.FILES)

        if outgoing_doc_form.is_valid():
            newdoc = outgoing_doc_form.save()
            return redirect('records:outgoingDoc')  #pk=newdoc.id
            messages.success(request, 'Added')
        else:
            messages.error(request, 'Not  Added')
            
    context ={'outgoingDocForm': outgoing_doc_form} 
    return render(request, 'records/outgoingDocForm.html', context)   


def OutgoingDocDetails(request):
    return render(request, 'records/outgoingDocDetails.html')