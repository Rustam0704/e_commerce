from django import forms
from .models import Contact_us

class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = ['name', 'number', 'reason','subject']


