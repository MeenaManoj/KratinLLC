# from django.urls import path
# from . import views
# urlpatterns = [
#     path('request-assistance/', views.request_assistance, name='request_assistance'),
#     path('home', views.home, name='home')

    
    
#     # Add more paths for other views if needed
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('medication/', views.medication_list, name='medication_list'),
    path('emergency/', views.emergency_contacts, name='emergency_contacts'),
    path('financial/', views.financial_management, name='financial_management'),
    path('assistance/', views.request_assistance, name='request_assistance'),
    path('add_medication/', views.add_medication,name='add_medication'),

    path('edit_medication/<str:name>', views.edit_medication, name='edit_medication'),
    path('delete_medication/',views.delete_medication,name="delete_medication"),
    path('add_emergency_contacts/', views.add_emergency_contacts, name='add_emergency_contacts'),
    path('delete_emergency_contacts/', views.delete_emergency_contacts, name='delete_emergency_contacts'),

    path('add_financial_Management',views.add_financial_Management,name="add_financial_Management")
]
