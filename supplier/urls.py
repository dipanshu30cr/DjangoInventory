from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', BhajanView.as_view(), name="EmployeeView"),
     path('supplierForm/',supplierForm , name='supplierForm'),
     path('supplierTable/',supplierTable , name='supplierTable'),
     path('soft_delete_supplier/<int:supplier_id>/', soft_delete_supplier, name='soft_delete_supplier'),
     path('supplierEdit/<int:supplier_id>/', supplierEdit, name='supplierEdit'),
    
]