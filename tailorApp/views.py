from django.shortcuts import render,redirect
from tailorApp.models import ClothModel,ContactUsModel,ContactModel,SettingsModel,SizeModel,Mybasket
from django.views.generic import View
from django.contrib import messages
from django.http import Http404

class ClothView(View):
    def get(self,request,*args,**kwargs):
        clothes = ClothModel.objects.order_by("price")
        contacts = ContactUsModel.objects.all()
        settings = SettingsModel.objects.all()
        sizes = SizeModel.objects.all()

        
        context = {
            "clothes" : clothes,
            "contacts" : contacts,
            "settings" : settings,
            "sizes" : sizes
        }
        return render(request, 'index.html',context)
    

    def post(self,request,*args,**kwargs):
        cloth_id = request.POST.get("cloth_id")
        cloth = ClothModel.objects.get(id=cloth_id)

        if request.user.is_authenticated:
            Mybasket.objects.create(
                user = request.user,
                cloth = cloth
            )
        return redirect("mybasket")

        
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
    

#-----------------------------------------------------------------------
class MyBasketView(View):
    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            raise Http404
        
        mybaskets = Mybasket.objects.filter(
            user = request.user
        )
        total_price = 0
        for basket in mybaskets:
            total_price += basket.cloth.price

        context = {
            "mybaskets" : mybaskets,
            "total_price" : total_price,
        }

        return render(request,"mybasket.html",context)
    
    def post(self,request,*args,**kwargs):
        basket_id = request.POST.get("basket_id")
        basket = Mybasket.objects.get(id=basket_id)

        basket.delete()
        return redirect("mybasket")

    