from django.urls import path
from tailorApp import views

urlpatterns = [
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('mybasket/',views.MyBasketView.as_view(),name="mybasket")
]