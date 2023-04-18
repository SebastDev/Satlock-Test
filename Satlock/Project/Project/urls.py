from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('', views.index, name = 'index'),
]
