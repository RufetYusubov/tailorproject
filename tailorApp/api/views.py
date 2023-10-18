from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView,ListAPIView,CreateAPIView
from django.contrib.auth.models import User


from tailorApp.models import ClothModel,ContactModel,ContactUsModel,SizeModel
from tailorApp.api.serializers import (ClothSerializer,ContactSerializer,ContactUsSerializer,SizeSerializer,
                                       UserListSerializer,UserCreateSerializer,UserUpdateSerializer)

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
#-------------------------------------------------------------------------------------
class SizeListCreateAPIView(ListCreateAPIView):
    queryset = SizeModel.objects.all()
    serializer_class = SizeSerializer

class SizeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SizeModel.objects.all()
    serializer_class = SizeSerializer
    lookup_field = "id"
#------------------------------------------------------------------------------------

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = "pk"



