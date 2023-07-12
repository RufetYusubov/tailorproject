from django.shortcuts import render,redirect
from tailorApp.models import ClothModel,ContactUsModel,ContactModel,SettingsModel,SizeModel
from django.views.generic import View
from django.contrib import messages

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
