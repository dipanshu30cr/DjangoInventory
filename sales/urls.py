from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', BhajanView.as_view(), name="EmployeeView"),
    path('salesForm/',salesForm , name='salesForm'),
    path('salesMasterTable/',salesMasterTable , name='salesMasterTable'),
    path('salesDetailsTable/',salesDetailsTable , name='salesDetailsTable'),
    

]