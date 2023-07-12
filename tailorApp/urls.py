from django.urls import path
from tailorApp import views

urlpatterns = [
    path('index/', views.ClothView.as_view(),name='index'),
    path('contact/',views.ContactView.as_view(),name='contact'),
]