import json
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Speaker
# Create your views here.

def speakerlist(request):
    speakers =Speaker.objects.all()
    return render(request,'index.html',{'speakers':speakers})

def singlespeaker(request,pk):
    speaker=Speaker.objects.get(name=pk)
    return render(request,'singlespeaker.html',{'speaker':speaker})


def speakerjson(request):
    
   # Retrieve all data from your model
    data = Speaker.objects.all().values()  

    #convert your data in to JSON
    json_data = json.dumps(list(data), indent=4)

      # Save JSON to a file in your project directory
    with open('speaker.json', 'w') as file:
        file.write(json_data)

        # Return a response to the browser
    response = HttpResponse(content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="speaker.json"'
    response.write(json_data)
    #return response
    return JsonResponse(list(data), safe=False)