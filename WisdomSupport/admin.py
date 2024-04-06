from django.contrib import admin


# Register your models here.

from django.contrib import admin
from .models import Medication, EmergencyContact, FinancialTransaction, EmergencyRequest

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage', 'frequency', 'time_of_day', 'user')

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'user')

@admin.register(FinancialTransaction)
class FinancialTransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'amount', 'date', 'user')

@admin.register(EmergencyRequest)
class EmergencyRequestAdmin(admin.ModelAdmin):
    list_display = ('message', 'timestamp', 'user')
