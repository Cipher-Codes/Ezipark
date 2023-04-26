from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomerLogin, OwnerLogin
# Create your views here.


def index(request):
    return render(request, "index.html")


def cust_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pswd = request.POST['pswd']
        check = CustomerLogin.objects.filter(email=email, password=pswd)
        if check.count() == 1:
            return redirect('/home')
        else:
            return render(request, "cust_login.html", {'val': 'empty'})
    return render(request, "cust_login.html")


def home(request):
    if request.method == 'POST':
        pin = request.POST.get('pincode', False)
        data = OwnerLogin.objects.filter(pincode=pin)
        context = {}
        context['lis'] = []
        l = []
        for i in data:
            context['lis'].append(i)
            print(i.pincode)
            l.append(i)
        return render(request, "home.html", {'val': data, 'l': l})
    return render(request, "home.html")


def owner_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pincode = request.POST['pincode']
        pswd = request.POST['pswd']
        re_pswd = request.POST['re_pswd']
        print(email, pincode, pswd, re_pswd)
        if pswd == re_pswd:
            OwnerLogin.objects.create(
                email=email, password=pswd, pincode=str(pincode))
            return HttpResponse("Added!")
        else:
            return render(request, "owner_register.html", {'val': 'empty'})
    return render(request, "owner_register.html")


def logout(request):
    if request.method == 'POST':
        email = request.POST['email']
        pswd = request.POST['pswd']
        check = OwnerLogin.objects.filter(email=email, password=pswd)
    return HttpResponse("Logged Out !")


def owner_register(request):
    return render(request, "owner_register.html")
