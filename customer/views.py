import csv
import json
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Customer

from django.http import HttpResponse


# Create your views here.


class CustomerList(ListView):
    template_name = 'customer/customer-list.html'
    model = Customer
    context_object_name = 'customers'
    
    

class CustomerDetail(DetailView):
    template_name = 'customer/detail.html'
    model = Customer
    
    

def exporting_data(request):
    file_type = request.GET.get('file_type')
    if file_type == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="customers.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID','FULL NAME','EMAIL','PHONE NUMBER','ADDRESS','JOINED'])

        customers = Customer.objects.all().values_list('id','full_name','email','phone_number','address','joined')
        for customer in customers:
            writer.writerow(customer)

        return response
    
    elif file_type == 'json':
        response = HttpResponse(content_type='application/json')
        data = list(Customer.objects.all().values('id','full_name', 'email', 'phone_number', 'address','joined'))
        # response.content = json.dumps(data, indent=4)
        response.write(json.dumps(data, indent=4,default=str))
        response['Content-Disposition'] = 'attachment; filename=customers.json'
        return response

    
    
