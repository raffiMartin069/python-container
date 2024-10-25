from django import forms

class AuthenticationForm(forms.Form):
    user_name = forms.CharField(label='Username', max_length=100, widget=forms.EmailInput)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)