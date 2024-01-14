from django import forms

from .models import IncomingDoc, OutgoingDoc

class IncomingDocForm(forms.ModelForm):
    class Meta:
        model = IncomingDoc 
        fields = '__all__'
        widgets = { 
            'continuos_number': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),
            
            'book_no': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),

            'page_no': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),

            'year': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),

            'archive': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),

            'branch': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),
            'date': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),

            'sender': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),
            
            'receiver': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),

            'number': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),

            'Surrender_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),
    
            'Surrender_date': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),

            'register_number': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),
            
            'image': forms.FileInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number '
                }),

            'remarks': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500 ',
                'placeholder': 'Enter number ',
                'rows':2,
                }),

            
        }
