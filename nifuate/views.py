from django.shortcuts import render,redirect
from .models import Logo,OnlineMember
from django_countries import countries as django_countries

# Create your views here.

def home(request):
    logo=Logo.objects.all()
    context = {
        'logo':logo
    }
    return render(request,'index.html', context)


def dashboard(request):
    return render(request,'dashboard.html')

def add_online_member(request):
    logo=Logo.objects.all()
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        gender=request.POST.get('gender', 'NOT_SPECIFIED')
        country_code=request.POST.get('country', '')
        online=OnlineMember.objects.create(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,gender=gender,country=country_code)
        online.save()
        return redirect('dashboard')
    context={
        'logo':logo,
        'gender_choices': OnlineMember.GENGER_CHOICES,
        'country_choices':django_countries.countries
    }
    return render(request, 'add_online_member.html', context)