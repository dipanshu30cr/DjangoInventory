from django.shortcuts import render
from django.db.models import Sum
from inventory.models import Item
from purchase.models import PurchaseDetails
from sales.models import SalesDetails

def reportForm(request):
    items = Item.objects.filter(Itemstatus=1)
    
    report_data = []  
    
    for item in items:
        total_purchase_quantity = PurchaseDetails.objects.filter(ItemAssigned__ItemId=item.ItemId).aggregate(total=Sum('Quantity'))['total'] or 0
        total_sales_quantity = SalesDetails.objects.filter(ItemAssigned__ItemId=item.ItemId).aggregate(total=Sum('ItemQuantity'))['total'] or 0
        
        available_stock = total_purchase_quantity - total_sales_quantity
        
        report_data.append({
            'item_name': item.ItemName,
            'purchase_quantity': total_purchase_quantity,
            'sales_quantity': total_sales_quantity,
            'available_stock': available_stock
        })
    
    return render(request, 'reportForm.html', {
        'report_data': report_data
    })


