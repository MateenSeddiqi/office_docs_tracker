from django.shortcuts import render, redirect
from .models import IncomingDoc, OutgoingDoc
from .forms import IncomingDocForm, OutgoingDocForm
from django.contrib import messages



def records(request):
    return render (request, 'records/records.html')
    

# All Incoming Docs codes: 
#     Display Incoming Docs 
#     Add Incoming Docs
#     Update Incoming Docs 
#     Delete Incoming Docs 

def incomingDoc(request):  
    incomingDocs = IncomingDoc.objects.all()
    return render (request, 'records/incomingDocs.html', {
        'incomingDocs': incomingDocs,
        })


def addIncomingDoc(request):
    incoming_doc_form = IncomingDocForm()
    if request.method == 'POST':
        incoming_doc_form = IncomingDocForm(request.POST, request.FILES)
        if incoming_doc_form.is_valid():
            newdoc = incoming_doc_form.save()
            return redirect('records:incomingDoc')
            messages.success(request, ' Added')
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

def updateIncomingDoc(request, pk):
    updateIncoming = IncomingDoc.objects.get(id=pk)
    updateForm = IncomingDocForm(request.POST or None, instance=updateIncoming)
    if updateForm.is_valid():
        updateForm.save()
        messages.success(request, 'Record Updated')
        return redirect ('records:incomingDoc')
    return render(request, 'records/update_incoming.html', {'updateForm':updateForm})

def deleteIncomingDoc(request, pk):
    deleteIncoming = IncomingDoc.objects.get(id=pk)
    deleteIncoming.delete()
    messages.success(request, 'Record Delete')
    return redirect ('records:incomingDoc')



#All Outgoing Docs codes: 
#     Display Outgoing Docs 
#     Add Outgoing Docs
#     Update Outgoing Docs 
#     Delete Outgoing Docs 

def outgoingDoc(request):
    outgoingDocs = OutgoingDoc.objects.all()
    return render (request, 'records/outgoingDocs.html', {
        'outgoingDocs': outgoingDocs,
        })


def addOutgoingDoc(request):
    outgoing_doc_form = OutgoingDocForm()
    if request.method == 'POST':
        outgoing_doc_form = OutgoingDocForm(request.POST, request.FILES)

        if outgoing_doc_form.is_valid():
            newdoc = outgoing_doc_form.save()
            messages.success(request, "Record Added")
            return redirect('records:outgoingDoc')
        else:
            messages.error(request, 'Not  Added')
    context ={'outgoingDocForm': outgoing_doc_form} 
    return render(request, 'records/outgoingDocForm.html', context)   


def OutgoingDocDetails(request, pk):
    outgoingDetails= OutgoingDoc.objects.filter(id=pk)
    context = {
        'outgoingDetails':outgoingDetails
    }
    return render(request, 'records/outgoingDocDetails.html', context)

def updateOutgoingDoc(request, pk):
    updateOutgoing = OutgoingDoc.objects.get(id=pk)
    updateForm = OutgoingDocForm (request.POST or None, instance=updateOutgoing)
    if updateForm.is_valid():
        updateForm.save()
        messages.success(request, 'Record Updated')
        return redirect ('records:outgoingDoc')
    return render(request, 'records/update_outgoing.html', {'updateForm':updateForm})

def DeleteOutgoingDoc(request, pk):
    deleteOutgoing = OutgoingDoc.objects.get(id=pk)
    deleteOutgoing.delete()
    messages.success(request, "Record Deleted")
    return redirect ('records:outgoingDoc')