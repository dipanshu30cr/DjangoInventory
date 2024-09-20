# from django.shortcuts import render, redirect, get_object_or_404
# from .models import *
# from django.db import IntegrityError
# from django.utils import timezone
# from django.core.exceptions import ValidationError
# from django.http import JsonResponse

# # Create your views here.
# def userForm(request):
#     if request.method == "POST":
    
#         name=request.POST.get("name")
#         userName= request.POST.get("userName")
#         password= request.POST.get("password")
#         entryDate= request.POST.get("entryDate") or timezone.now()
#         userStatus=request.POST.get("userStatus", True)

#         u = User(name=name, userName=userName, password=password, 
#                  userStatus=userStatus, entryDate=entryDate)

#         try:
#                 u.save()
#                 return redirect('/userForm')
#         except ValidationError as e:
#                 error_message = f"Validation Error: {str(e)}"
#                 return render(request, "userFormForm.html", {"error_message": error_message})

#     current_date = timezone.now().strftime('%Y-%m-%d')
#     return render(request, "userForm.html", {'current_date': current_date})

# def userTable(request):
#     users = User.objects.all()  # Fetch all vehicles
#     print()
#     return render(request, "userTable.html", {'users': users})


# # def soft_delete_supplier(request, user_id):
# #     if request.method == "POST":
# #         try:
# #             user = User.objects.get(pk=user_id)
# #             user.UserStatus = 0  # Set status to 0 (soft deleted)
# #             user.save()
# #             return JsonResponse({'success': True})
# #         except User.DoesNotExist:
# #             return JsonResponse({'success': False, 'error': 'User not found'})
# #     return JsonResponse({'success': False, 'error': 'Invalid request method'})

# def soft_delete_user(request, user_id):

#     if request.method == "POST":
#         try:
#             user = User.objects.get(pk=user_id)
#             user.userStatus = 0  
#             user.save()
#             return JsonResponse({'success': True})
#         except User.DoesNotExist:
#             return JsonResponse({'success': False, 'error': 'Item not found'})
#     return JsonResponse({'success': False, 'error': 'Invalid request method'})


# # def loginForm(request):
# #     # nameOfSession= User.objects.get(userName= userName)
# #     # request.session[nameOfSession]= 'userName'
# #     # userName= request.session.get(nameOfSession)
# #     # context= ('userName':userName)
# #     error_message = None
    
# #     if request.method == "POST":
# #         userName = request.POST.get("userName")
# #         password = request.POST.get("password")

# #         try:
# #             user = User.objects.get(userName=userName)
            
# #             if user.password == password:
# #                 return redirect('/itemTable')
# #             else:
# #                 error_message = "Invalid password. Please try again."
# #         except User.DoesNotExist:
# #             error_message = "User does not exist. Please check your username."

# #     return render(request, "loginForm.html", {"error_message": error_message})

# def loginForm(request):
#     error_message = None
#     userName = None
    
#     if request.method == "POST":
#         userName = request.POST.get("userName")
#         password = request.POST.get("password")
#         name= request.POST.get("name")

#         try:
#             user = User.objects.get(userName=userName)
            
#             if user.password == password:
                
#                 request.session['userName'] = user.userName
#                 request.session['password'] = user.password
#                 request.session['name'] = user.name

#                 return redirect('/itemTable')
#             else:
#                 error_message = "Invalid password. Please try again."
#         except User.DoesNotExist:
#             error_message = "User does not exist. Please check your username."

#     return render(request, "loginForm.html", {"error_message": error_message, "userName": userName})


# def logout_view(request):
#     request.session.flush()
#     return redirect('/loginForm')


from django.shortcuts import render, redirect
from django.utils import timezone
from .models import User, UserSession
from django.http import JsonResponse
from django.core.exceptions import ValidationError


def userForm(request):
    if request.method == "POST":
        name = request.POST.get("name")
        userName = request.POST.get("userName")
        password = request.POST.get("password")
        entryDate = request.POST.get("entryDate") or timezone.now()
        userStatus = request.POST.get("userStatus", True)

        u = User(name=name, userName=userName, password=password, 
                 userStatus=userStatus, entryDate=entryDate)

        try:
            u.save()
            return redirect('/userForm')
        except ValidationError as e:
            error_message = f"Validation Error: {str(e)}"
            return render(request, "userForm.html", {"error_message": error_message})

    current_date = timezone.now().strftime('%Y-%m-%d')
    return render(request, "userForm.html", {'current_date': current_date})

def userTable(request):
    users = User.objects.all()
    return render(request, "userTable.html", {'users': users})

def soft_delete_user(request, user_id):
    if request.method == "POST":
        try:
            user = User.objects.get(pk=user_id)
            user.userStatus = 0  
            user.save()
            return JsonResponse({'success': True})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Item not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def loginForm(request):
    error_message = None

    if request.method == "POST":
        userName = request.POST.get("userName")
        password = request.POST.get("password")

        try:
            user = User.objects.get(userName=userName)
            if user.password == password:
                session = UserSession(user=user, login_time=timezone.now())
                session.save()

                request.session['userName'] = user.userName
                request.session['password'] = user.password
                # request.session['name'] = user.name

                return redirect('/itemTable')
            else:
                error_message = "Invalid password. Please try again."
        except User.DoesNotExist:
            error_message = "User does not exist. Please check your username."

    return render(request, "loginForm.html", {"error_message": error_message})

def logout_view(request):
    
    userName = request.session.get('userName')
    if userName:
        try:
            session = UserSession.objects.filter(user__userName=userName).latest('login_time')
            session.logout_time = timezone.now()
            session.save()
        except UserSession.DoesNotExist:
            #error_message = "User session does not exist. Please check your username."
            pass

    request.session.flush()
    return redirect('/loginForm')

def indexForm(request):
    sessions = UserSession.objects.all()
    print(sessions)
    return render(request, "indexForm.html", {'report_data': sessions})
