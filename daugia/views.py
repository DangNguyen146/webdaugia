from django.shortcuts import render, redirect

from .models import *
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout


def Home(request):
    data = 0
    error = ""
    user = ""
    try:
        user = User.objects.get(username=request.user.username)
    except:
        pass
    try:
        data = BidderUser.objects.get(user=user)
        if data:
            error = "pat"
            return redirect('profile1')
    except:
        pass
    try:
        data = AuctionUser.objects.get(user=user)
        return redirect('trainer_home')
    except:
        pass
    d = {'error': error, 'data': data}
    return render(request, 'carousel.html', d)


def Home(request):
    result = ''
    data = 0
    user = ''
    try:
        user = User.objects.get(username=request.user.username)
    except:
        pass

    try:
        data = BidderUser.objects.get(user=user)
        if data:
            result = "bidder"
            # return redirect('profile1')
    except:
        pass

    try:
        data = AuctionUser.objects.get(user=user)
        result = "seller"
        # return redirect('trainer_home')
    except:
        pass

    d = {'result': result, 'data': data}
    return render(request, 'homepage.html', d)


def LoginUser(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        result = ''
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if (user):
            try:
                sign = BidderUser.objects.get(user=user)
                result = "bidder"
            except:
                result = "seller"
            login(request, user)
        else:
            result = 'not'
            d = {'result': result}
            return render(request, 'login.html', d)
        d = {'result': result, 'isLogin': True}
        return render(request, 'homepage.html', d)


def Register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        email = request.POST['email']

        username = request.POST['username']
        password = request.POST['password']

        contact = request.POST['contact']
        address = request.POST['address']
        dob = request.POST['dob']

        reg = request.POST['reg']
        image = request.FILES['image']

        user = User.objects.create_user(
            first_name=first_name, last_name=last_name, email=email, username=username, password=password)

        membership = MemberFee.objects.get(fee="Unpaid")
        if reg == "Bidder":
            BidderUser.objects.create(
                membership=membership, user=user, contact=contact, address=address, dob=dob, image=image)
        else:
            AuctionUser.objects.create(
                membership=membership, user=user, contact=contact, address=address, dob=dob, image=image)
        d = {'result': 'register'}
        return render(request, 'login.html',  d)


def Logout(request):
    logout(request)
    return redirect('home')
