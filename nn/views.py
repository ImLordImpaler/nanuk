from django.shortcuts import render , redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate , logout , login
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginPage')
def index(request):
    return render(request , 'nn/index.html')

def reasons(request):
    pass
@login_required(login_url='loginPage')
def gallery(request):
    return render(request , 'nn/gallery.html')
def loginPage(request):
    if request.method == 'POST':
        email1 = request.POST.get('email')
        passwd = request.POST.get('passwd')

        user = authenticate(request , email1 , passwd)
        if user is not None:
            login(request , user)
        else:
            print('andha hai kya lawde')
    return render(request , 'nn/login.html')
@login_required(login_url='loginPage')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            print('andha hai kya lawde')
    else:
        form = NewUserForm()

    params = {
        'form': form
    }
    return render(request , 'nn/register.html', params)