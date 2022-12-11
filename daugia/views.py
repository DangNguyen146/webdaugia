from django.shortcuts import render, redirect

from .models import *
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

# ///////////////// homepage


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
        return redirect('home')


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
        return redirect('loginUser')


def Logout(request):
    logout(request)
    return redirect('home')


# def new():
#     status = Status.objects.get(status="pending")
#     new_pro = Product.objects.filter(status=status)
#     return new_pro


def ProfileUser(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    data = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
        return render(request, 'profileUser.html', d)
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
        return render(request, 'profileUser.html', d)


def EditProfileUser(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    user = ''
    data = ''
    try:
        user = User.objects.get(username=request.user.username)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    except:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}

    if request.method == "GET":
        return render(request, 'editProfile.html', d)
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        contact = request.POST['contact']
        address = request.POST['address']

        try:
            data.image = request.FILES['image']
            data.save()
        except:
            pass
        user.first_name = first_name
        user.last_name = last_name
        data.address = address
        data.contact = contact

        user.save()
        data.save()

        d = {'result': "editprofile", 'data': data}
        return render(request, 'profileUser.html', d)


def ChangePassword(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    user = ''
    data = ''
    try:
        user = User.objects.get(username=request.user.username)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    except:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}

    if request.method == "GET":
        return render(request, 'editPassword.html', d)
    if request.method == "POST":
        pw1 = request.POST['pw1']
        pw2 = request.POST['pw2']
        pw3 = request.POST['pw3']
        if (pw2 == pw3):
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(pw2)
            u.save()
            d = {'result': "changepassword", 'data': data}
            return render(request, 'login.html', d)
        else:
            d = {'result': "passnot", 'data': data}
            return render(request, 'editPassword.html', d)


def ManagerWallet(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    data = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    log = ''
    log = MemberFeeLog.objects.filter(user=user).order_by('-created_at')
    try:
        print("----------------------------------")
        print(log)

        d = {'data': data, 'log': log}
    except:
        pass
    return render(request, 'managerwallet.html', d)


def AddMoneyToWallet(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    data = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    if request.method == "GET":
        return render(request, 'addmoneytowallet.html', d)
    if request.method == "POST":
        mem = MemberFee.objects.get(fee="Paid")
        data.membership = mem
        data.allMoney += 10000
        data.save()

        MemberFeeLog.objects.create(
            user=user, nameLog="Add money", status="0", money=10000)

        return redirect('wallet')


# ///////////////// homepage


# ///////////////// admin

def new():
    status = Status.objects.get(status="Pending")
    new_pro = Product.objects.filter(status=status)
    return new_pro


def AdminHome(request):
    if not request.user.is_staff:
        return redirect('home')

    new2 = new()
    count = 0
    if new2:
        count += 1

    all_p = 0
    all_b = 0
    all_s = 0
    pro = Product.objects.all()
    bid = BidderUser.objects.all()
    sel = AuctionUser.objects.all()

    for i in pro:
        all_p += 1
    for i in bid:
        all_b += 1
    for i in sel:
        all_s += 1

    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    d = {'data': data, 'result': result, 'count': count, 'new2': new2,
         'all_p': all_p, 'all_b': all_b, 'all_s': all_s}
    return render(request, 'dashboardadminpage.html', d)


def AdminAddSeactionDate(request):
    if not request.user.is_staff:
        return redirect('home')

    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    if request.method == 'POST':
        d = request.POST['date']
        SessionDate.objects.create(date=d)
        return redirect('adminviewsectiondate')
    return render(request, 'addsectiondate.html', d)


def AdminViewSeactionDate(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    cat = SessionDate.objects.all()
    d = {'data': data, 'result': result, 'date1': cat}
    return render(request, 'viewsectiondate.html', d)


def EditSessiondate(request, pid):
    if not request.user.is_staff:
        return redirect('home')

    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)

    ses = SessionDate.objects.get(id=pid)
    d = {'data': data, 'result': result, 'ses': ses}

    if request.method == 'POST':
        n = request.POST['date']
        ses.date = n
        ses.save()
        return redirect('adminviewsectiondate')
    return render(request, 'editsectiondate.html', d)


def Deletesessiondate(request, pid):
    cat = SessionDate.objects.get(id=pid)
    cat.delete()
    return redirect('adminviewsectiondate')


def AdminAddSeactionTime(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    return render(request, 'addsectiontime.html', d)


def AdminViewSeactionTime(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    return render(request, 'viewsectiontime.html', d)


def AdminAddCategory(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    return render(request, 'addcategory.html', d)


def AdminViewCategory(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    return render(request, 'viewcategory.html', d)


def AdminAddSubcategory(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    return render(request, 'addsubcategory.html', d)


def AdminViewSubcategory(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    return render(request, 'viewsubcategory.html', d)


def AdminAddProducionVerification(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    return render(request, 'addproducionverification.html', d)


def AdminViewProducionVerification(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    return render(request, 'viewproducionverification.html', d)


def AdminBidderUserManager(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    return render(request, 'bidderuser.html', d)


def AdminSellerUserManager(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    return render(request, 'selleruser.html', d)


def AdminResult(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    return render(request, 'result.html', d)


def AdminFeedBack(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
        d = {'data': data, 'result': result}
    return render(request, 'feedBack.html', d)
    # ///////////////// admin
