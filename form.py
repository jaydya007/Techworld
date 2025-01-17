from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name*', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email*', 'required': True}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject*', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone*', 'required': True}),
            'message': forms.Textarea(attrs={'placeholder': 'Message*', 'required': True}),
            
        }
