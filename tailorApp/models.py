from django.db import models
from django.contrib.auth.models import User

class SizeModel(models.Model):
    size_name = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Size'

    def __str__(self) -> str:
        return self.size_name
    

class ClothModel(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField(default=0)
    discountPrice = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to="posters/")
    about = models.TextField()
    sizes = models.ManyToManyField(SizeModel,blank=True,null=True,related_name="clothes")

    class Meta:
        verbose_name = 'Cloth'
        verbose_name_plural = 'Clothes'


    def __str__(self) -> str:
        return self.name
      

class ContactUsModel(models.Model):
    email = models.EmailField()
    telephone = models.CharField(max_length=100)
    streetadres = models.CharField(max_length=200)
    about = models.TextField()

    class Meta:
        verbose_name_plural = 'With us contact'

    def __str__(self) -> str:
        return self.email
       
class ContactModel(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact'

    def __str__(self) -> str:
        return self.name + " " + self.surname
    
