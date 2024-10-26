from django import forms

class AuthenticationForm(forms.Form):
    email = forms.CharField(label='Email Address', max_length=100, widget=forms.EmailInput(attrs={'class':'form-control', 'id': 'email_address'}))
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}))