from django.urls import path
from tailorApp.api import views

urlpatterns = [
    path('clothes-list-create/',views.ClothListCreateAPIView.as_view()),
    path('cloth-retrieve-update-delete/<int:id>/',views.ClothRetrieveUpdateDestroyAPIView.as_view()),
    path('contacts-list-create/',views.ContactListCreateAPIView.as_view()),
    path('contact-retrieve-update-delete/<int:id>/',views.ContactRetrieveUpdateDestroyAPIView.as_view()),
    path('contactus-list-create/',views.ContactUsListCreateAPIView.as_view()),
    path('contactus-retrieve-update-delete/<int:id>/',views.ContactUsRetrieveUpdateDestroyAPIView.as_view()),
    path('settings-list-create/',views.SettingsListCreateAPIView.as_view()),
    path('setting-retrieve-update-delete/<int:id>/',views.SettingsRetrieveUpdateDestroyAPIView.as_view()),
    path('sizes-list-create/',views.SizeListCreateAPIView.as_view()),
    path('size-retrieve-update-delete/<int:id>/',views.SizeRetrieveUpdateDestroyAPIView.as_view()),
    path('mybaskets-list-create/',views.MybasketListCreateAPIView.as_view()),
    path('mybasket-retrieve-update-delete/<int:id>/',views.MybasketRetrieveUpdateDestroyAPIView.as_view()),
]