from django import forms

from .models import IncomingDoc, OutgoingDoc

class IncomingDocForm(forms.ModelForm):
    class Meta:
        model = IncomingDoc 
        fields = ('')