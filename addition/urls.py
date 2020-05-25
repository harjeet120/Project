
from django.urls import path
from.import views

urlpatterns = [
    path('',views.addition,name='addition'),
    path('result',views.result,name="result"),

]
