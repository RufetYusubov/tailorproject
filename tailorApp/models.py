from django.db import models
from django.contrib.auth.models import User

class SizeModel(models.Model):
    size_name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.size_name
    

class ClothModel(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="posters/")
    size = models.ManyToManyField(SizeModel,blank=True,null=True,related_name="clothes")


    def __str__(self) -> str:
        return self.name
      

class ContactUsModel(models.Model):
    email = models.EmailField()
    telephone = models.CharField(max_length=100)
    streetadres = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.email
    
class SettingsModel(models.Model):
    banner_image = models.ImageField(upload_to='posters/', blank=True,null=True)
    banner_title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='posters/', blank=True,null=True)
    about = models.TextField()

    def __str__(self) -> str:
        return self.about
    
class ContactModel(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Mybasket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_basket_clothes")
    cloth = models.ForeignKey(ClothModel,on_delete=models.CASCADE,related_name="my_clothes")

    def __str__(self) -> str:
        return self.user.username
