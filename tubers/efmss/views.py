from django.shortcuts import render,redirect
from .models import Efms
from django.contrib import messages
# Create your views here.

def efms(request):
    if request.method == 'POST':
        full_name=request.POST['full_name']
        phone=request.POST['phone']
        email=request.POST['email']
        company=request.POST['company']
        subject=request.POST['subject']
        message=request.POST['message']

        efms=Efms(full_name=full_name, phone=phone, email=email, company=company, subject=subject, message=message)
        efms.save()
        messages.success(request,"We will Get Back to you ASAP")
        return redirect('youtubers')

