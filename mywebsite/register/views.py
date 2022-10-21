from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method== 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')

    return render(request,'login.html')
def registration(request):
    if request.method== 'POST':
        username=request.POST['user_name']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Alredy Exists")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('registration')
            else:
                user=User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
                user.save()
                messages.info(request,"User Saved")
                return redirect('login')
        else:
            messages.info(request,"Password Not Matched")
            return redirect('registration')
        return redirect('/')
    return render(request,'registration.html')
def logout(request):
    auth.logout(request)
    return redirect('/')