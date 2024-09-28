from django.shortcuts import render,redirect
from .models import Logo
from django.utils import timezone


# Create your views here.

def home(request):
    logo=Logo.objects.all()
    context = {
        'logo':logo
        
    }
    return render(request,'index.html', context)


def dashboard(request):
    logo=Logo.objects.all()
    time=timezone.now()
    context = {
        'logo':logo,
        'month':time.strftime('%B'),
        'year':time.year
    }
    return render(request,'dashboard.html',context)

