from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView


from tailorApp.models import ClothModel,ContactModel,ContactUsModel,SettingsModel,SizeModel,Mybasket
from tailorApp.api.serializers import (ClothSerializer,ContactSerializer,ContactUsSerializer,
                                       SettingsSerializer,MybasketSerializer,SizeSerializer)

class ClothListCreateAPIView(ListCreateAPIView):
    queryset = ClothModel.objects.all()
    serializer_class = ClothSerializer

class ClothRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ClothModel.objects.all()
    serializer_class = ClothSerializer
    lookup_field = "id"
#--------------------------------------------------------------------------------
class ContactListCreateAPIView(ListCreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "id"
#-------------------------------------------------------------------------------------

class ContactUsListCreateAPIView(ListCreateAPIView):
    queryset = ContactUsModel.objects.all()
    serializer_class = ContactUsSerializer

class ContactUsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContactUsModel.objects.all()
    serializer_class = ContactUsSerializer
    lookup_field = "id"
#---------------------------------------------------------------------------------------

class SettingsListCreateAPIView(ListCreateAPIView):
    queryset = SettingsModel.objects.all()
    serializer_class = SettingsSerializer

class SettingsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SettingsModel.objects.all()
    serializer_class = SettingsSerializer
    lookup_field = "id"
#-------------------------------------------------------------------------------------
class SizeListCreateAPIView(ListCreateAPIView):
    queryset = SizeModel.objects.all()
    serializer_class = SizeSerializer

class SizeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SizeModel.objects.all()
    serializer_class = SizeSerializer
    lookup_field = "id"
#---------------------------------------------------------------------
class MybasketListCreateAPIView(ListCreateAPIView):
    queryset = Mybasket.objects.all()
    serializer_class = MybasketSerializer

class MybasketRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Mybasket.objects.all()
    serializer_class = MybasketSerializer
    lookup_field = "id"



