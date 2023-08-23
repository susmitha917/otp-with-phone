from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .manager import UserManager



# Create your models here.
class User(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=14,unique=True)
    is_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=6,null=True,blank=True)
    
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def name(self):
        return self.first_name + ' ' + self.last_name
    
    def _self_(self):
        return self.phone_number
