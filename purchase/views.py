from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import PurchaseMaster, PurchaseDetails
from inventory.models import Item
from supplier.models import Supplier
import json


def purchaseForm(request):
    suppliers = Supplier.objects.filter(Supplierstatus=1)
    items = Item.objects.filter(Itemstatus=1)

    if request.method == "POST":
        supplier_id = request.POST.get("supplier")
        purchase_details_json = request.POST.get("purchase_details")  
        total_amount = request.POST.get("totalAmount")
        
        try:
            
            purchase_master = PurchaseMaster.objects.create(
                PurchaseMasterReference=generate_reference_number(),
                PurchaseMasterTotal=total_amount,
                PurchaseMasterDate=timezone.now(),
                PurchaseSupplier_id=supplier_id,
                PurchaseMasterstatus=1,
            )

            
            purchase_details = json.loads(purchase_details_json)
            
            
            for detail in purchase_details:
                item_id = detail['itemId']
                quantity = detail['quantity']
                amount = detail['amount']

                
                PurchaseDetails.objects.create(
                    PurchaseMasterAssigned=purchase_master,
                    ItemAssigned_id=item_id,
                    Quantity=quantity,
                    Amount=amount,
                    PurchaseDetailsstatus=1,
                    PurchaseDetailsEntryDate=timezone.now(),
                )

            
            return redirect('/purchaseForm')

        except Exception as e:
            
            return redirect('/purchaseForm')

    return render(request, 'purchaseForm.html', {'suppliers': suppliers, 'items': items})

def generate_reference_number():
    return "REF" + str(timezone.now().strftime('%Y%m%d%H%M%S'))

def purchaseMasterTable(request):
    purchase_masters = PurchaseMaster.objects.all()  # Fetch all purchase master records
    return render(request, "purchaseMasterTable.html", {'purchase_masters': purchase_masters})


def purchaseDetailsTable(request):
    purchase_details = PurchaseDetails.objects.all()  # Fetch all purchase details records
    return render(request, "purchaseDetailsTable.html", {'purchase_details': purchase_details})
