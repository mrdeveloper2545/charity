from django.shortcuts import render,redirect
from .models import Logo,OnlineMember
from .forms import OnlineMemberForm

# Create your views here.

def home(request):
    logo=Logo.objects.all()
    context = {
        'logo':logo
    }
    return render(request,'index.html', context)


def dashboard(request):
    logo=Logo.objects.all()
    context = {
        'logo':logo
    }
    return render(request,'dashboard.html',context)

def add_online_member(request):
    logo=Logo.objects.all()
    if request.method == 'POST':
        form=OnlineMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            form=OnlineMemberForm()
    context={
        'logo':logo,
        'form':OnlineMemberForm(),
    }
    return render(request, 'add_online_member.html', context)