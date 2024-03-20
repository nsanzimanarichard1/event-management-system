from django.urls import path
from . import views

urlpatterns=[
    path('participant/',views.participantlist,name="participantlist"),
    path('participant/<str:pk>/',views.singleparticipant,name="single participant")
]