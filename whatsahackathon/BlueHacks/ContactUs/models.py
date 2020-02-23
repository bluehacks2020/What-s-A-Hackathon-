from django.db import models

# Create your models here.
class ContactEntry(models.Model):
    contact_name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=30)
    email_addr = models.CharField(max_length=100)
    position = models.CharField(max_length=30)
