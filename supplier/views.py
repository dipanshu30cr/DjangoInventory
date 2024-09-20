from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db import IntegrityError
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.http import JsonResponse



def supplierForm(request):
    if request.method == "POST":
        SupplierName = request.POST.get("SupplierName")
        SupplierAddress = request.POST.get("SupplierAddress")
        SupplierContact= request.POST.get("SupplierContact")
        Supplierstatus = request.POST.get("Supplierstatus", True)  # Default to True

        SupplierEntryDate = request.POST.get("SupplierEntryDate") or timezone.now()

        UserId = request.POST.get("UserId")

        i = Supplier(SupplierName=SupplierName, SupplierAddress=SupplierAddress, SupplierContact=SupplierContact, 
                 Supplierstatus=Supplierstatus, SupplierEntryDate=SupplierEntryDate, UserId=UserId)

        try:
            i.full_clean()  
            i.save()
            return redirect('/supplierTable')
        except ValidationError as e:
            error_message = f"Validation Error: {str(e)}"
            return render(request, "supplierForm.html", {"error_message": error_message})

    current_date = timezone.now().strftime('%Y-%m-%d')
    user_uuid = str(uuid.uuid4())

    return render(request, "supplierForm.html", {'current_date': current_date, 'user_uuid': user_uuid})


def supplierTable(request):
    suppliers = Supplier.objects.all()  # Fetch all vehicles
    print()
    return render(request, "supplierTable.html", {'suppliers': suppliers})


def soft_delete_supplier(request, supplier_id):
    if request.method == "POST":
        try:
            supplier = Supplier.objects.get(pk=supplier_id)
            supplier.Supplierstatus = 0  # Set status to 0 (soft deleted)
            supplier.save()
            return JsonResponse({'success': True})
        except Supplier.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Supplier not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



def supplierEdit(request, supplier_id):
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    
    if request.method == "POST":
        SupplierName = request.POST.get("SupplierName")
        SupplierContact = request.POST.get("SupplierContact")
        SupplierAddress= request.POST.get("SupplierAddress")
        # Ensure valid input
        if Supplier.objects.filter(SupplierContact=SupplierContact).exclude(pk=supplier_id).exists():
            error_message = "Supplier with this contact number already exists."
            return render(request, "supplierEdit.html", {"error_message": error_message, "supplier": supplier})

        # Update the supplier
        supplier.SupplierName = SupplierName
        supplier.SupplierContact = SupplierContact
        supplier.SupplierAddress=SupplierAddress

        try:
            supplier.full_clean()  # Run validations
            supplier.save()
            return redirect('/supplierTable')
        except ValidationError as e:
            error_message = f"Validation Error: {str(e)}"
            return render(request, "supplierEdit.html", {"error_message": error_message, "supplier": supplier})
        except IntegrityError:
            error_message = "Contact number must be unique. Please enter a different Contact number."
            return render(request, "supplierEdit.html", {"error_message": error_message, "supplier": supplier})

    return render(request, "supplierEdit.html", {"supplier": supplier})