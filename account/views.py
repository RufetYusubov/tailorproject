from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views import View

def check_password(password):
    if len(password)>=8:
        return True
    return False

def check_validation(password):
    has_digit, has_alpha, has_symbols = False, False, False

    for i in password:
        if i.isdigit():
            has_digit =  True
        elif i.isalpha():
            has_alpha = True
        else:
            has_symbols = True
    return has_digit and has_alpha and has_symbols

class SignupView(View):
    def get(self,request,*args,**kwargs):
    
        return render(request,'signup.html')
    
    def post(self,request,*args,**kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not User.objects.filter(username=username).exists():
            if not check_password(password) :
                messages.info(request, "Password must be at least 8 symbols")
                return redirect('signup')
            elif not check_validation(password):
                messages.info(request,"Password must contain both characters and numbers")
                return redirect('signup')
            else:
                User.objects.create_user(
                username = username,
                password = password
            )
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You logged in.")
                return redirect("index")
        else:
            messages.info(request,"Username has been taken")
            return redirect("signup")
        
#--------------------------------------------------------------------------------------------------
class LoginUserView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')
    
    def post(self,request,*args,**kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "You logged in.")
            return redirect("index")
        else:
            if not User.objects.filter(username=username).exists():
                messages.info(request,"Please enter correct username")
            else:
                messages.info(request,"Please, enter correct password")
            return redirect("login")
#-----------------------------------------------------------------------------------------
def logoutUser(request):
    logout(request)
    return redirect("index")
#------------------------------------------------------------------------------------------
class ChangepasswordView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'changepassword.html')
    
    def post(self,request,*args,**kwargs):
        username = request.POST.get("username")
        newpassword1 = request.POST.get("newpassword1")
        newpassword2 = request.POST.get("newpassword2")
        user = User.objects.get(username=username)

        if newpassword1 == newpassword2:
            user.set_password(newpassword1)
            user.save()
            messages.success(request, "Password changed")

        return redirect("login")
