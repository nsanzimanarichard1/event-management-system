
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Participant
# Create your views here.

def participantlist(request):
    participants = Participant.objects.all()
    return render(request,'participant.html',{'participants':participants})

def singleparticipant(request,pk):
    participant=Participant.objects.get(email=pk)
    return render(request,'singleparticipant.html',{'participant':participant})

def participantjson(request):
    
   # Retrieve all data from your model
    data = Participant.objects.all().values()  

    #convert your data in to JSON
    json_data = json.dumps(list(data), indent=4)

      # Save JSON to a file in your project directory
    with open('participant.json', 'w') as file:
        file.write(json_data)

        # Return a response to the browser
    response = HttpResponse(content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="participant.json"'
    response.write(json_data)
    #return response
    return JsonResponse(list(data), safe=False)