from django import forms

class AuthenticationForm(forms.Form):
    email = forms.CharField(label='Email Address', max_length=100, required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'id': 'email_address'}), error_messages={'required': 'Email address is required.'})
    password = forms.CharField(label='Password', max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}), error_messages={'required': 'Password is required.'})

class SignUpForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'id': 'first_name'}), error_messages={'required': 'First name is required.'})
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.
    TextInput(attrs={'class':'form-control', 'id': 'last_name'}), error_messages={'required': 'Last name is required.'})
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'id': 'gender', 'class': 'form-select'}),
        label="Gender"
    )
    age = forms.CharField(label='Age', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'id': 'age'}), error_messages={'required': 'Age is required.'})
    address = forms.CharField(label='Address', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'id': 'home_address'}), error_messages={'required': 'Address is required.'})
    email = forms.CharField(label='Email Address', max_length=100, widget=forms.EmailInput(attrs={'class':'form-control', 'id': 'email_address'}), error_messages={'required': 'Email address is required.'})
    password = forms.CharField(label='Password', min_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}), error_messages={'required': 'Password is required.'})
    confirm_password = forms.CharField(label='Confirm Password', min_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'confirm_password'}), error_messages={'required': 'Confirm password is required.'})

    def password_match(self):
        password = super().clean()['password']
        confirm_password = super().clean()['confirm_password']

        if password != confirm_password:
            super().add_error(None, 'Password does not match.')
            return False
        return True
        