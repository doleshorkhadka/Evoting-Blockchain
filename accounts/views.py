from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import *
from .models import *
from dashboard.functions import accounts
from django.contrib.auth.models import Group

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form=UserForm(request.POST)
        profile_form=register_form(data=request.POST,files=request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            user_group = Group.objects.get(name='ElectionUser') 
            user.groups.add(user_group)

            profile.save()
            print('Only user is saved')
            # newprofile = Profile(phone_num=p_num)
            # log the user in
            login(request,user)
            messages.info(request, 'You are registered Successfully.')
            return redirect('accounts:login')
        else:
            messages.alert(request, 'Signup failed (Something missing) !!')
    else:
        form = UserForm()
        profile_form = register_form()

    context = {
        'form':form ,
        'profile':profile_form,
    }
    return render(request,'accounts/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request,user)
            messages.info(request, 'Login Successfully.')
            return redirect('dashboard:dash')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):

    # Form POST banako bela ra yo jhan secure method ho #
    # if request.method == 'POST': #
    #     logout(request) #
    #     return redirect('landing_page') #

    logout(request)
    messages.info(request, 'Logout Successfully.')
    return redirect('landing_page')

def address_creation():
    print("Accessing users ..")
    users = Profile.objects.all()
    print("Assigning addresses to the users")
    print(len(users),users)
    # ganache_url = "http://127.0.0.1:8545"
    # web3 = Web3(Web3.HTTPProvider(ganache_url))
    for x in range(11,11+len(users)):
        # address = web3.toChecksumAddress(account['address'])
        obj = Profile.objects.get(id = x)
        obj.token = accounts[x-11]
        obj.save()
