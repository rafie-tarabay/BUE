from . import views
from django.urls import path
from django.views.generic.base import RedirectView

app_name="main"

urlpatterns = [
                path('home/', views.home),
                path('login/', views.login),
                path('upload/', views.upload),
                path('NewUser/', views.NewUser,name='newuser'),
                
                path('Messages1/', views.MyFormView.as_view(), name='MyFormView'),


                path('', RedirectView.as_view(url='main/home/')),
              ]

