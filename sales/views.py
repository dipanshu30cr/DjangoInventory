
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import SalesMaster, SalesDetails
from inventory.models import Item
import json
from purchase.models import *
from django.http import JsonResponse
from django.db.models import Sum

def generate_reference_number():
    
    return "REF" + str(timezone.now().strftime('%Y%m%d%H%M%S'))


def salesMasterTable(request):
    sales_masters = SalesMaster.objects.all() 
    return render(request, "salesMasterTable.html", {'sales_masters': sales_masters})


def salesDetailsTable(request):
    sales_details = SalesDetails.objects.all() 
    return render(request, "salesDetailsTable.html", {'sales_details': sales_details})

def salesForm(request):
    items = Item.objects.filter(Itemstatus=1)  # Fetch active items

    if request.method == 'POST':
        CustomerName = request.POST.get("CustomerName")
        CustomerPhone = request.POST.get("CustomerPhone")
        sales_details_json = request.POST.get("sales_details")
        SalesDate = request.POST.get("SalesDate")
        total_amount = request.POST.get("totalAmount")

        try:
            sales_details = json.loads(sales_details_json)  

            for detail in sales_details:
                item_id = detail['itemId']
                entered_quantity = int(detail['quantity'])
                total_purchase_quantity = PurchaseDetails.objects.filter(ItemAssigned_id=item_id).aggregate(total=models.Sum('Quantity'))['total']

                if not total_purchase_quantity:
                    error_message = "This item is not available in the purchase records."
                    return render(request, "salesForm.html", {"error_message": error_message})

                total_sold_quantity = SalesDetails.objects.filter(ItemAssigned_id=item_id).aggregate(total=models.Sum('ItemQuantity'))['total'] or 0

                available_stock = total_purchase_quantity - total_sold_quantity

                if entered_quantity > available_stock:
                    error_message = f"Only {available_stock} units of this item are available."
                    return render(request, "salesForm.html", {"error_message": error_message})

            sales_master = SalesMaster.objects.create(
                CustomerName=CustomerName,
                CustomerPhone=CustomerPhone,
                SalesMasterReference=generate_reference_number(),
                SalesDate=SalesDate,
                SalesMasterTotal=total_amount,
                SalesMasterstatus=1,
                SalesMasterEntryDate=timezone.now(),
            )

            for detail in sales_details:
                SalesDetails.objects.create(
                    ItemAssigned_id=detail['itemId'],
                    ItemQuantity=detail['quantity'],
                    ItemPrice=detail['price'],
                    ItemAmount=detail['amount'],
                    SalesMasterId=sales_master,
                    SalesDetailsstatus=1,
                    SalesDetailEntryDate=timezone.now(),
                )

            return redirect('/salesMasterTable') 
        except Exception as e:
            print(f"Error: {e}") 
            return redirect('/salesForm')  

    return render(request, 'salesForm.html', {'items': items})



