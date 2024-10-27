from django.db import models

# Create your models here.
class Authentication(models.Model):
    email = models.CharField(max_length=100, unique=True, blank=False, null=False, error_messages={'unique': 'This email address is already in use.'})
    password = models.CharField(max_length=100, blank=False, null=False, error_messages={'blank': 'Password cannot be empty.'})

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_user_credentials(self):
        if self.email != 'rafael@gmail.com' or self.password != '123456':
            return False
        return True
    
    def user_not_exist(self):
        return 'User not found! Try again.'
    
    def user_exist(self):
        return 'User found!'