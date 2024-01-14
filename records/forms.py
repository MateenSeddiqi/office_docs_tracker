from django import forms

from .models import IncomingDoc, OutgoingDoc

class IncomingDocForm(forms.ModelForm):
    class Meta:
        model = IncomingDoc 
        fields = '__all__'
        # fields = ('continuos_number', 'book_no', 'page_no', 'year', 'archive', 'branch', 'date', 'sender', 'receiver', 'number', 'Surrender_name', 'Surrender_date', 'register_number', 'remarks', 'image', )
