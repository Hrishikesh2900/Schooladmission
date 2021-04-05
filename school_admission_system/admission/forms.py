from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'address','marks', 'password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-comtrol'}),
            'email':forms.EmailInput(attrs={'class':'form-comtrol'}),
            'address':forms.TextInput(attrs={'class':'form-comtrol'}),
            'marks':forms.TextInput(attrs={'class':'form-comtrol'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-comtrol'}),

        }