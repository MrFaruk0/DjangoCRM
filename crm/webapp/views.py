from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateClientForm, UpdateClientForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Client
from django.contrib import messages


# Create your views here.

#home page
def home(request):
    return render(request, 'webapp/index.html')


#register page 

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Account created successfully! You can now login.')

            return redirect('my-login')

    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)


#login page
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                messages.success(request, 'Login successful!')

                return redirect("dashboard")

    context = {'form': form}
    return render(request, 'webapp/my-login.html', context=context)

#dashboard page

@login_required(login_url='my-login')
def dashboard(request):

    clients = Client.objects.all()
    context= {'clients': clients}

    return render(request, "webapp/dashboard.html", context=context)

#Create client 

@login_required(login_url='my-login')
def create_client(request):

    form = CreateClientForm()

    if request.method == 'POST':
        form = CreateClientForm(request.POST)

        if form.is_valid():
            
            form.save()

            messages.success(request, 'Client created successfully!')
            return redirect('dashboard')
        
    context = {'form': form}
    return render(request, 'webapp/create.html', context=context)


#Update client
@login_required(login_url='my-login')
def update_client(request, pk):

    client = Client.objects.get(id=pk)
    form = UpdateClientForm(instance=client)

    if request.method == 'POST':
        form = UpdateClientForm(request.POST, instance=client)

        if form.is_valid():

            form.save()

            messages.success(request, 'Client updated successfully!')
            return redirect('dashboard')
        
    context = {'form': form}
    return render(request, 'webapp/update.html', context=context)

#View client details
@login_required(login_url='my-login')
def view_client(request, pk):

    client = Client.objects.get(id=pk)
    context = {'client': client}

    return render(request, 'webapp/view.html', context=context)

#Delete client
@login_required(login_url='my-login')
def delete_client(request, pk):
    client = Client.objects.get(id=pk)

    client.delete()

    messages.success(request, 'Client deleted successfully!')
    return redirect('dashboard')






#logout page
def user_logout(request):
    
    auth.logout(request)
    return redirect("my-login")