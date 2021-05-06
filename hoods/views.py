from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Neighborhood, Profile, Business, Alert, Hospital
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .forms import RegisterForm, NewBusinessForm, ProfileUpdateForm, NewAlertForm
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = User.objects.get(username=username)
            profile=Profile.objects.create(user=user,email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request,'registration/registration_form.html')

@login_required
def index(request):
    hoods = Neighborhood.objects.all()
    return render(request,'index.html',{'hoods':hoods})
    
@login_required
def join(request,hood_id):
    user = request.user
    hood= Neighborhood.objects.get(pk=hood_id)
    Profile.objects.filter(user=user).update(neighborhood=hood)
    return redirect('home')

@login_required
def home(request):
    hoods = Neighborhood.objects.all()
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if profile.neighborhood:
        hood = Neighborhood.objects.get(pk=profile.neighborhood.id)
        count = Profile.objects.filter(neighborhood=hood).count()
        businesses = Business.objects.filter(neighborhood=hood).all()
        alerts = Alert.objects.filter(hood=hood).all()
        if request.method == 'POST':
            user=request.user
            form = NewAlertForm(request.POST)
            if form.is_valid():
                alert=form.save(commit=False)
                alert.user=current_user
                alert.hood=hood
                alert.save()
                return redirect('home')
        else:
            form=NewAlertForm
    else:
        return redirect('index')
    return render(request, 'home.html',{'hood':hood,'hoods':hoods,'count':count,'alerts':alerts,'businesses':businesses,'form':form})

@login_required
def my_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form=ProfileUpdateForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
    context={
        'form':form,
        'profile':profile,
    }
    return render(request,"my_profile.html",context=context)

def leave(request):
    user = request.user
    Profile.objects.filter(user=user).update(neighborhood=None)
    return redirect('index')

def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search(search_term)
        print(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/') 
def business(request,business_id):
    business=Business.objects.get(id=business_id)
    return render(request,"business.html",{"business":business})

def newbusiness(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewBusinessForm(request.POST)
        if form.is_valid():
                business=form.save(commit=False)
                business.neighborhood=current_user.profile.neighborhood
                print(business.neighborhood)
                business.save()
                return redirect('home')
    else:
        form = NewBusinessForm()
    return render(request,'Newbusiness.html',{'form':form})
