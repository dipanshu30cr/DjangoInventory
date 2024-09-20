from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db import IntegrityError
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.http import JsonResponse




# def home(request):
#     print("addEmp is here")
#     return render(request, "Item_Main.html" ,{})
 
def itemForm(request):
    if request.method == "POST":
        ItemName = request.POST.get("ItemName")
        ItemRate = request.POST.get("ItemRate")
        Itemstatus = int(request.POST.get("Itemstatus", 1))  

        ItemEntryDate = request.POST.get("ItemEntryDate") or timezone.now()

        UserId = request.POST.get("UserId")

        
        if Item.objects.filter(ItemName=ItemName).exists():
            error_message = "Item with this name already exists."
            return render(request, "itemForm.html", {"error_message": error_message})

        
        i = Item(ItemName=ItemName, ItemRate=ItemRate, Itemstatus=Itemstatus, 
                 ItemEntryDate=ItemEntryDate, UserId=UserId)

        try:
            # Run validatii.full_clean()  ons
            i.save()
            return redirect('/itemTable')
        except ValidationError as e:
            error_message = f"Validation Error: {str(e)}"
            return render(request, "itemForm.html", {"error_message": error_message})
        except IntegrityError:
            error_message = "Item name must be unique. Please enter a different item name."
            return render(request, "itemForm.html", {"error_message": error_message})

    current_date = timezone.now().strftime('%Y-%m-%d')
    user_uuid = str(uuid.uuid4())

    return render(request, "itemForm.html", {'current_date': current_date, 'user_uuid': user_uuid})


def itemTable(request):
    items = Item.objects.all()  
    return render(request, "itemTable.html", {'items': items})

def soft_delete_item(request, item_id):
    if request.method == "POST":
        try:
            item = Item.objects.get(pk=item_id)
            item.Itemstatus = 0  
            item.save()
            return JsonResponse({'success': True})
        except Item.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Item not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


def itemEdit(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    if request.method == "POST":
        ItemName = request.POST.get("ItemName")
        ItemRate = request.POST.get("ItemRate")

        # Ensure valid input
        if Item.objects.filter(ItemName=ItemName).exclude(pk=item_id).exists():
            error_message = "Item with this name already exists."
            return render(request, "itemEdit.html", {"error_message": error_message, "item": item})

        item.ItemName = ItemName
        item.ItemRate = ItemRate

        try:
            item.full_clean()
            item.save()
            return redirect('/itemTable')
        except ValidationError as e:
            error_message = f"Validation Error: {str(e)}"
            return render(request, "itemEdit.html", {"error_message": error_message, "item": item})
        except IntegrityError:
            error_message = "Item name must be unique. Please enter a different item name."
            return render(request, "itemEdit.html", {"error_message": error_message, "item": item})

    return render(request, "itemEdit.html", {"item": item})


    
