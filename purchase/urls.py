from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', BhajanView.as_view(), name="EmployeeView"),
     path('purchaseForm/',purchaseForm , name='purchaseForm'),
     path('purchaseMasterTable/',purchaseMasterTable , name='purchaseMasterTable'),
     path('purchaseDetailsTable/',purchaseDetailsTable , name='purchaseDetailsTable'),
     
    
]