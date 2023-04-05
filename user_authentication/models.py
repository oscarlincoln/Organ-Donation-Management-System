from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class user(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_donor_patient = models.BooleanField('Is donor or recipient', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)
    
