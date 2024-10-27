from django import forms

class AuthenticationForm(forms.Form):
    email = forms.CharField(label='Email Address', max_length=100, required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'id': 'email_address'}), error_messages={'required': 'Email address is required.'})
    password = forms.CharField(label='Password', max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}), error_messages={'required': 'Password is required.'})

class SignUpForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'id': 'first_name'}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'id': 'last_name'}))
    gender = forms.CharField(label='Gender', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'id': 'gender'}))
    age = forms.CharField(label='Age', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'id': 'age'}))
    address = forms.CharField(label='Address', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'id': 'home_address'}))
    email = forms.CharField(label='Email Address', max_length=100, widget=forms.EmailInput(attrs={'class':'form-control', 'id': 'email_address'}))
    password = forms.CharField(label='Password', min_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}))
    confirm_password = forms.CharField(label='Confirm Password', min_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'confirm_password'}))