from django.shortcuts import render,redirect
from tailorApp.models import ClothModel,ContactUsModel,ContactModel,SizeModel
from django.views.generic import View
from django.contrib import messages
from django.http import Http404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


class ClothView(View):
    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            raise Http404
        clothes = ClothModel.objects.order_by("price")
        contacts = ContactUsModel.objects.all()
        sizes = SizeModel.objects.all()

        
        context = {
            "clothes" : clothes,
            "contacts" : contacts,
            "sizes" : sizes
        }
        return render(request, 'index.html',context)
            
#-----------------------------------------------------------
class ContactView(View):
    def get(self,request,*args,**kwargs):

        return render(request,"contact.html")
    
    def post(self,request,*args,**kwargs):
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        telephone = request.POST.get("telephone")
        message = request.POST.get("message")

        ContactModel.objects.create(
            name = name,
            surname = surname,
            email = email,
            telephone = telephone,
            message = message
        )
        messages.success(request,"Message sent")

        return redirect("contact") 
    
#---------------------------------------------------------------------
class DetailView(View):
    def get(self,request,id,*args,**kwargs):
        if not request.user.is_authenticated:
            raise Http404
        
        cloth = ClothModel.objects.get(id=id)
        sizes = SizeModel.objects.all()
        contacts = ContactUsModel.objects.all()

        context = {
            "cloth" : cloth,
            "sizes" : sizes,
            "contacts" : contacts
        }

        return render(request,"detail.html",context)
    

#-----------------------------------------------------------------------
# ------------------------- Signup Login  -------------------------------------------
def check_password(password):
    if len(password)>=8:
        return True
    return False

def check_validation(password):
    has_digit, has_lower_case, has_upper_case = False, False,False

    for i in password:
        if i.isdigit():
            has_digit =  True
        elif i.isalpha() and i.isupper():
            has_upper_case = True
        elif i.isalpha() and i.islower():
            has_lower_case = True
    return has_digit and has_lower_case and has_upper_case

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
    return redirect("login")
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

    