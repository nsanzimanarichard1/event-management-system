from django.urls import path

from . import views

urlpatterns=[
    path('payment/',views.payment,name='payment'),
    path('payment/<str:pk>/',views.singlepayment,name="single")
]