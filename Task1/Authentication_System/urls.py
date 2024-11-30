from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",auth_views.LoginView.as_view(template_name='Authentication_System/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('signup/',views.signup,name="signup"),
    path('home/',views.home,name="home")

]
