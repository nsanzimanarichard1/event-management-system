import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Event,Schedule
from django.utils import timezone
from Paymentmethod.models import Payment
from Speaker.models import Speaker
from  Participant.models import Participant
from .forms import EventForm
def index(request): 

    events = Event.objects.all()[:15]
    speakers =Speaker.objects.all()[:15]
    schedules = Schedule.objects.all()[:15]

    context = {'events':events,
               'speakers':speakers,
               'schedules':schedules
               }
    return render(request, 'index.html',context)

def singleEvent(request,pk):
    event = Event.objects.get(title=pk)
    context = {'event':event}
    return render(request,'details.html',context)

def schedule(request): #schedule 
    schedules = Schedule.objects.all()
    context = {'schedules':schedules}
    return render(request, 'schedule.html',context)

def free_event(request):
    free_events = Event.objects.filter(isfree=True)
    return render(request,'freeEvent.html',{'free_events':free_events})

def paidevent(request): #free event 
    payments = Payment.objects.all().filter(payment_status='PAID').values()
    context = {'payment':payments}
    return render(request,'paidevent.html',context)

def register(request):
    form = EventForm()

    context = {'form':form}
    return render(request,'register.html',context)

   
def eventjson(request):#json event database
 # Retrieve all data from your model
    data = Event.objects.all().values()  

    #convert your data in to JSON
    json_data = json.dumps(list(data), indent=4)

      # Save JSON to a file in your project directory
    with open('event.json', 'w') as file:
        file.write(json_data)

        # Return a response to the browser
    response = HttpResponse(content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="event.json"'
    response.write(json_data)
    #return response
    return JsonResponse(list(data), safe=False)

def paid_events(request):
    paidEvents = Event.objects.filter(is_Paid=False)
    return render(request, 'event_list.html', {'events': paidEvents})








