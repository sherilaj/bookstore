from django import forms
from . models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['Name','EmailId','Message','Subject']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'EmailId': forms.EmailInput(attrs={'class': 'form-control'}),
            'Message': forms.Textarea(attrs={'class': 'form-control'}),
            'Subject': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        
        