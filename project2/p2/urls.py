
from django.contrib import admin
from django.urls import path

from django.urls import include
from django.views.generic.base import RedirectView

urlpatterns = [
                path('main/', include('main.urls')),
                path('admin/', admin.site.urls),
                path('', RedirectView.as_view(url='main/home/')),
              ]

