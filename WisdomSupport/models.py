from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Medication(models.Model):
    user = models.ForeignKey(User,default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    time_of_day = models.TimeField()

class EmergencyContact(models.Model):
    user = models.ForeignKey(User,default=1 ,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

class FinancialTransaction(models.Model):
    user = models.ForeignKey(User,default=1, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class EmergencyRequest(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)