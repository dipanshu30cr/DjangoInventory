"""
URL configuration for inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('itemTable/',itemTable , name='itemTable'),
    path('itemForm/',itemForm , name='itemForm'),
    path('itemTable/',itemTable , name='itemTable'),
    path('soft_delete_item/<int:item_id>/', soft_delete_item, name='soft_delete_item'),
    path('itemEdit/<int:item_id>/', itemEdit, name='itemEdit'),
    path('', include('supplier.urls')),
    path('', include('purchase.urls')),
    path('', include('sales.urls')),
    path('', include('report.urls')),
    path('', include('user.urls')),

    

    
]
