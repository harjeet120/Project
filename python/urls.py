"""python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from python.view import paymentMode
from webapp import views
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.home,name='home'),
    path('paymentMode/<int:pk>/', paymentMode, name='paymentMode'),
    path('register', view.register, name='register'),
    path('home',view.home,name='home'),
    path('about',view.about,name='about'),
    path('contact',view.contact,name='contact'),
    path('page',view.page,name='page'),
    path('login',view.login,name='login'),
    path('detail',view.detail,name='detail'),
    path('places',view.places,name='places'),
    path('booking/<int:package_id>',view.booking,name='booking'),
   #path('',include ('travello.urls')),
]