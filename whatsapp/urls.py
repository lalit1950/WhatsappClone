from django.contrib import admin
from django.urls import path
from whatsapp import views
from django.conf import settings
from django.conf.urls.static import static
from .views import * 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
]
