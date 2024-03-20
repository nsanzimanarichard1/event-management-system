import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .models import Payment

# Create your views here.

def payment(request):
 payments = Payment.objects.all()
 context ={'payments':payments}
 return render(request,'payment.html',context)

def singlepayment(request,pk):
   payment = Payment.objects.get(id=pk)
   context = {'payment':payment}
   return render(request,'singlepayment.html',context)


def paymentjson(request):
 # Retrieve all data from your model
    data = Payment.objects.all().values()  

    #convert your data in to JSON
    json_data = json.dumps(list(data), indent=4)

      # Save JSON to a file in your project directory
    with open('payment.json', 'w') as file:
        file.write(json_data)

        # Return a response to the browser
    response = HttpResponse(content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="payment.json"'
    response.write(json_data)
    #return response
    return JsonResponse(list(data), safe=False)
