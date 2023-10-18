from django.urls import path
from tailorApp.api import views

urlpatterns = [
    path('clothes-list-create/',views.ClothListCreateAPIView.as_view()),
    path('cloth-retrieve-update-delete/<int:id>/',views.ClothRetrieveUpdateDestroyAPIView.as_view()),
    path('contacts-list-create/',views.ContactListCreateAPIView.as_view()),
    path('contact-retrieve-update-delete/<int:id>/',views.ContactRetrieveUpdateDestroyAPIView.as_view()),
    path('contactus-list-create/',views.ContactUsListCreateAPIView.as_view()),
    path('contactus-retrieve-update-delete/<int:id>/',views.ContactUsRetrieveUpdateDestroyAPIView.as_view()),
    path('sizes-list-create/',views.SizeListCreateAPIView.as_view()),
    path('size-retrieve-update-delete/<int:id>/',views.SizeRetrieveUpdateDestroyAPIView.as_view()),
     path('user-list/', views.UserListAPIView.as_view()),
    path('user-create/',views.UserCreateAPIView.as_view()),
    path('user-retrieve-update-delete/<int:pk>/',views.RetrieveUpdateDestroyAPIView.as_view()),
]