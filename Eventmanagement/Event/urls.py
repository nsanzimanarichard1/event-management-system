from django.urls import path

from .import views

urlpatterns = [
     path('', views.index, name='index'),
     path('schedule/', views.schedule, name='index'),
     path('event/<str:pk>/',views.singleEvent, name="singleEvent"),
     path('freeEvent/', views.free_event, name='freeEvent'),
     path('eventcount/', views.paidevent, name='paidEvent'),
     path('eventAttended/', views.free_event, name='freeEvent'),
     path('paidevent/', views.paidevent, name='paidevent'),
    path('eventjson/',views.eventjson,name="eventjSon"),
    path('register/',views.register,name="register"),
    #path('event_total_amount_paid/<int:event_id>/', views.event_total_amount_paid, name='event_total_amount_paid'),
    #path('participantAttended/',views.participantsAttended,name='eventAttended'),


     ] 
