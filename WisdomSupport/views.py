# from django.shortcuts import render

# # Create your views here.


# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from .models import Medication, EmergencyContact, FinancialTransaction, EmergencyRequest
# from .forms import MedicationForm, EmergencyContactForm, FinancialTransactionForm, EmergencyRequestForm

# @login_required
# def request_assistance(request):
#     if request.method == 'POST':
#         form = EmergencyRequestForm(request.POST)
#         if form.is_valid():
#             emergency_request = form.save(commit=False)
#             emergency_request.user = request.user
#             emergency_request.save()
#             # Add code to notify caregivers or emergency services
#             return redirect('home')  # Redirect to home page or a confirmation page
#     else:
#         form = EmergencyRequestForm()
#     return render(request, 'WisdomSupport/request_assistance.html', {'form': form})


# def home(request):
#     return render(request,'WisdomSupport/home.html')


from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from django.shortcuts import redirect, render

from .forms import EmergencyContactForm, FinancialTransactionForm, MedicationForm
from .models import EmergencyContact, FinancialTransaction, Medication

def home(request):
    return render(request, 'WisdomSupport/home.html')

# def medication_list(request):
    
#     # Implement medication list logic here
#     return render(request, 'WisdomSupport/medication_list.html')


def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'WisdomSupport/medication_list.html', {'medications': medications})

def add_medication(request):
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medication_list')
    else:
        form = MedicationForm()
    return render(request, 'WisdomSupport/add_medication.html', {'form': form})

def edit_medication(request, name):
    medication = get_object_or_404(Medication, name=name)
    if request.method == 'POST':
        form = MedicationForm(request.POST, instance=medication)
        if form.is_valid():
            form.save()
            return redirect('medication_list')
    else:
        form = MedicationForm(instance=medication)
    return render(request, 'WisdomSupport/edit_medication.html', {'medication': medication, 'form': form})




def delete_medication(request):
    if request.method == 'POST':
        medication_name = request.POST.get('medication_id')  # Change variable name
        # Get all medications with the given name
        medications = Medication.objects.filter(name=medication_name)
        # Delete all medications with the given name
        medications.delete()
        return JsonResponse({"result":"delete data successfully"})  # Redirect to some page after deletion
    else:
        # Handle GET requests if needed
        pass


def emergency_contacts(request):
    emergency_contacts = EmergencyContact.objects.all()
    return render(request, 'WisdomSupport/emergency_contacts.html', {'emergency_contacts': emergency_contacts})


def add_emergency_contacts(request):
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emergency_contacts')
        else:
            print(form.errors)
    else:
        form = EmergencyContactForm()  
    return render(request, 'WisdomSupport/emergency_contacts.html', {'form': form})



def delete_emergency_contacts(request):
    if request.method == 'POST':
        emergency_contacts_name = request.POST.get('contact_id')
        medications = EmergencyContact.objects.filter(name=emergency_contacts_name)
        medications.delete()
        return JsonResponse({"result":"delete data successfully"})
    else:
        pass




def financial_management(request):

    financial_transactions = FinancialTransaction.objects.all()
    return render(request, 'WisdomSupport/financial_Management.html', {'financial_transactions': financial_transactions})



def add_financial_Management(request):
    if request.method == 'POST':
        form = FinancialTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financial_management')
        else:
            print(form.errors)
    else:
        form = FinancialTransactionForm()  
    return render(request, 'WisdomSupport/financial_Management.html', {'form': form})


def request_assistance(request):
    # Implement request assistance logic here
    return render(request, 'WisdomSupport/request_assistance.html')
