from django.urls import path
from tailorApp import views

urlpatterns = [
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('detail/<int:id>/',views.DetailView.as_view(),name='detail'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('changepassword/',views.ChangepasswordView.as_view(), name= 'changepassword'),
]