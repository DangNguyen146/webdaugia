from django.shortcuts import render, redirect

from .models import *
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout


import datetime
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
    result = ''
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
    result = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
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
    result = ''
    result = ''
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
    result = ''
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
    result = ''

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
    if data.membership.fee == "Unpaid":
        d = {'data': data, 'result': result, 'Unpaid': 'Unpaid'}
        return render(request, 'managerwallet.html', d)
    log = ''
    log = MemberFeeLog.objects.filter(user=user).order_by('-created_at')

    d = {'data': data, 'log': log}
    return render(request, 'managerwallet.html', d)


def AddMoneyToWallet(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    data = ''
    user = User.objects.get(username=request.user.username)
    result = ''

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
    result = ''
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
    result = ''
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
    if request.method == 'POST':
        d = request.POST['date']
        SessionDate.objects.create(date=d)
        return redirect('adminviewsectiondate')
    return render(request, 'addsectiondate.html', d)


def AdminViewSeactionDate(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    result = ''
    data = ''
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
    result = ''
    data = ''
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
    result = ''
    data = ''
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
    sed = SessionDate.objects.all()

    if request.method == 'POST':
        d = request.POST['date']
        t = request.POST['time']
        d1 = SessionDate.objects.get(date=d)
        SessionTime.objects.create(date=d1, time=t)
        return redirect('adminviewsectiontime')
    d = {'data': data, 'result': result, 'sed': sed}
    return render(request, 'addsectiontime.html', d)


def AdminViewSeactionTime(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    result = ''
    data = ''
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
    cat = SessionTime.objects.all()
    d = {'data': data, 'result': result, 'time1': cat}
    return render(request, 'viewsectiontime.html', d)


def DeletesessionTime(request, pid):
    cat = SessionTime.objects.get(id=pid)
    cat.delete()
    return redirect('adminviewsectiontime')


def EditSessionTime(request, pid):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    result = ''
    data = ''
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

    sed = SessionDate.objects.all()
    sett = SessionTime.objects.get(id=pid)

    if request.method == 'POST':
        d = request.POST['date']
        t = request.POST['time']
        sedd = SessionDate.objects.get(id=d)
        sett.date = sedd
        sett.time = t
        sett.save()
        return redirect('adminviewsectiontime')

    d = {'data': data, 'result': result, 'sed': sed, 'sett': sett}
    return render(request, 'editsectiontime.html', d)


def AdminAddCategory(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    result = ''
    data = ''
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
    if request.method == 'POST':
        n = request.POST['cat']
        Category.objects.create(name=n)
        return redirect('adminviewcategory')
    d = {'data': data, 'result': result}
    return render(request, 'addcategory.html', d)


def EditCategory(request, pid):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    result = ''
    data = ''
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
    cat = Category.objects.get(id=pid)
    if request.method == 'POST':
        n = request.POST['cat']
        cat.name = n
        cat.save()
        return redirect('adminviewcategory')

    d = {'data': data, 'result': result, 'cat': cat}
    return render(request, 'editcategory.html', d)


def DeleteCategory(request, pid):
    cat = Category.objects.get(id=pid)
    cat.delete()
    return redirect('adminviewcategory')


def AdminViewCategory(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    result = ''
    data = ''
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
    cat = Category.objects.all()
    d = {'data': data, 'result': result, 'cat': cat}
    return render(request, 'viewcategory.html', d)


def AdminAddSubcategory(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    result = ''
    data = ''
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
    cat = Category.objects.all()
    if request.method == 'POST':
        n = request.POST['cat']
        s = request.POST['scat']
        cat1 = Category.objects.get(name=n)
        SubCategory.objects.create(name=s, category=cat1)
        return redirect('adminviewsubcategory')
    d = {'data': data, 'result': result, 'cat': cat}
    return render(request, 'addsubcategory.html', d)


def EditSubCategory(request, pid):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    result = ''
    data = ''
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
    cat = Category.objects.all()
    subcat = SubCategory.objects.get(id=pid)
    if request.method == 'POST':
        n = request.POST['cat']
        s = request.POST['scat']
        subcat.category = Category.objects.get(name=n)
        subcat.name = s
        subcat.save()
        return redirect('adminviewsubcategory')
    d = {'data': data, 'result': result, 'cat': cat, 'subcat': subcat}
    return render(request, 'editsubcategory.html', d)


def DeleteSubCategory(request, pid):
    cat = SubCategory.objects.get(id=pid)
    cat.delete()
    return redirect('adminviewsubcategory')


def AdminViewSubcategory(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    result = ''
    data = ''
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
    cat = SubCategory.objects.all()
    d = {'data': data, 'result': result, 'cat': cat}
    return render(request, 'viewsubcategory.html', d)


def AdminAddProducionVerification(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    data = ''
    result = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    prod = AuctedProduct.objects.all()
    d = {'data': data, 'result': result, 'prod': prod}
    return render(request, 'addproducionverification.html', d)


def AdminViewProducionVerification(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    result = ''
    data = ''
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

    prod = AuctedProduct.objects.all()
    d = {'data': data, 'result': result, 'prod': prod}
    return render(request, 'viewproducionverification.html', d)


def AdminBidderUserManager(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    result = ''
    data = ''
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
    prod = BidderUser.objects.all()
    d = {'data': data, 'result': result, 'prod': prod}
    return render(request, 'bidderuser.html', d)


def AdminSellerUserManager(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    result = ''
    data = ''
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
    prod = AuctionUser.objects.all()
    d = {'data': data, 'result': result, 'prod': prod}
    return render(request, 'selleruser.html', d)


def AdminResult(request):
    if not request.user.is_staff:
        return redirect('home')
    user = User.objects.get(username=request.user.username)
    result = ''
    data = ''
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
    result = ''
    data = ''
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


# ///////////////////// product
def LoadCourses(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    programming_id = request.GET.get('programming')
    # programming_id1 = request.GET.get('programming1')
    # print(programming_id,11111111111111111,programming_id1)
    courses = SubCategory.objects.filter(
        category_id=programming_id).order_by('name')
    # courses1 = Session_Time.objects.filter(date_id=programming_id1).order_by('name')
    return render(request, 'courses_dropdown_list_options.html', {'courses': courses})


def LoadCourses1(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    programming_id = request.GET.get('programming')
    courses = SessionTime.objects.filter(date_id=programming_id)
    return render(request, 'courses_dropdown_list_options1.html', {'courses': courses})


def AddProduct(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')

    data = ''
    result = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)

    if data.membership.fee == "Unpaid":
        return redirect('wallet')
    cat = Category.objects.all()
    scat = SubCategory.objects.all()
    sell = AuctionUser.objects.get(user=user)
    date1 = datetime.date.today()
    sed = SessionDate.objects.all()
    sett = SessionTime.objects.all()
    if request.method == "POST":
        c = request.POST['cat']
        s = request.POST['scat']
        p = request.POST['p_name']
        pr = request.POST['price']
        i = request.FILES['image']
        sett1 = request.POST['time']
        sed1 = request.POST['date']

        sub = SubCategory.objects.get(id=s)
        ses = SessionTime.objects.get(id=sett1)
        sta = Status.objects.get(status="Pending")
        pro1 = Product.objects.create(
            status=sta, session=ses, category=sub, name=p, min_price=pr, images=i)
        auc = AuctedProduct.objects.create(
            product=pro1, user=sell)
        return redirect('home')
    d = {'data': data, 'result': result, 'sed': sed, 'sett': sett, 'cat': cat, 'scat': scat,
         'date1': date1}
    return render(request, 'addproduct.html', d)


def ProductDetail2(request, pid):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    data = ''
    result = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    pro = Product.objects.get(id=pid)
    prod = AuctedProduct.objects.all()
    end = pro.session.time.split(':')

    if end[0] == "23":
        end1 = "00"
    else:
        end1 = str(int(end[0]) + 1)
    end2 = end1 + ":" + end[1]

    d = {'data': data, 'result': result, 'prod': prod, 'pro': pro, 'end2': end2}
    return render(request, 'productdetail2.html', d)


def ChangeStatus(request, pid):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    data = ''
    result = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)

    pro1 = Product.objects.get(id=pid)
    if request.method == "POST":
        stat = request.POST['stat']
        sta = Status.objects.get(status=stat)
        pro1.status = sta
        pro1.save()
        return redirect('adminaddproducionverification')
    d = {'pro': pro1,  'result': result, 'data': data, }
    return render(request, 'status.html', d)


def AllProduct(request):
    data = ''
    result = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    if data.membership.fee == "Unpaid":
        return redirect('wallet')
    pro = AuctedProduct.objects.filter(user=data)
    d = {'data': data,  'result': result, 'pro': pro}
    return render(request, 'allproduct.html', d)


def ApiParticipateduser(request, pid):
    auc = AuctedProduct.objects.get(id=pid)
    pro1 = Participant.objects.filter(aucted_product=auc).count()
    d = {'data': pro1, }
    return render(request, 'apiauctionuserallproduct.html', {'data': pro1})


def ParticipatedUser(request, pid):
    data = ''
    result = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    if data.membership.fee == "Unpaid":
        return redirect('wallet')

    auc = AuctedProduct.objects.get(id=pid)
    pro1 = Participant.objects.filter(aucted_product=auc)
    if not pro1:
        message1 = "No Bidder"
    d = {'data': data,  'result': result,
         'pro1': pro1, 'message1': message1, 'auc': auc}
    return render(request, 'participateduserproduct.html', d)


def BiddingStatus2(request):
    data = ''
    result = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    if data.membership.fee == "Unpaid":
        return redirect('wallet')

    pro1 = AuctedProduct.objects.filter(user=data)
    d = {'data': data,  'result': result, 'pro': pro1}

    return render(request, 'bidding_status2.html', d)


def ViewAuction(request):
    data = ''
    result = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    if data.membership.fee == "Unpaid":
        return redirect('wallet')

    terror = False
    if request.method == "POST":
        pro1 = Product.objects.get(id=pid)
        auc = AuctedProduct.objects.get(product=pro1)
        Participant.objects.create(user=data, aucted_product=auc)
        terror = True
    pid = 0
    d1 = Participant.objects.filter(user=data)
    li = []
    for i in d1:
        li.append(i.aucted_product.product.id)

    status = Status.objects.get(status="Accept")
    pro = Product.objects.filter(status=status)
    pro1 = Product.objects.all()
    message1 = ""
    if not pro:
        message1 = " No Any Bidding Product "
    for i in pro:
        if i.id in li:
            i.temp = 1
            i.save()
        else:
            i.temp = 0
            i.save()
    for i in pro:
        a = i.session.date.date
        li = a.split('-')
        total_time = (int(li[0]) * 365) + (int(li[1]) * 30) + (int(li[2]))
        d1 = datetime.date.today()
        d2 = datetime.datetime.now()
        c_time = d2.strftime("%H:%M")
        y = d1.year
        m = d1.month
        d = d1.day
        now_total = (int(y) * 365) + (int(m) * 30) + (int(d))
        part = Participant.objects.all()
        for l in part:
            z = l.aucted_product.product.session.date.date
            li2 = z.split('-')
            total_time_part = (int(li2[0]) * 365) + \
                (int(li2[1]) * 30) + (int(li2[2]))
            if total_time_part < now_total:
                if l.result is None:
                    r = Result.objects.get(result="notproper")
                    l.result = r
                    l.save()
        li2 = i.session.time.split(':')
        li3 = c_time.split(':')
        time1 = (int(li2[0]) * 60) + int(li2[1])
        time2 = (int(li3[0]) * 60) + int(li3[1])
        time3 = time1 + 60
        if total_time == now_total:
            if time1 == time2:
                i.temp = 2
                i.save()
            elif time2 < time3 and time2 > time1:
                i.temp = 2
                i.save()
            elif time2 > time3:
                i.temp = 3
                i.save()
        elif total_time < now_total:

            i.temp = 3
            i.save()
    d = {'pro': pro1, 'data': data, 'result': result, 'message1': message1}

    return render(request, 'viewauction.html', d)


def ViewAuction1(request, pid):
    data = ''
    result = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    if data.membership.fee == "Unpaid":
        return redirect('wallet')

    if request.method == "POST":
        pro1 = Product.objects.get(id=pid)
        auc = AuctedProduct.objects.get(product=pro1)
        Participant.objects.create(
            user=data, aucted_product=auc, product_id=pid)
        return redirect('home')
    return redirect('home')


def productdetail(request, pid):
    data = ''
    result = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    if data.membership.fee == "Unpaid":
        return redirect('wallet')

    pro = Product.objects.get(id=pid)
    end = pro.session.time.split(':')
    end1 = ""
    if end[0] == "23":
        end1 = "00"
    else:
        end1 = str(int(end[0])+1)
    end2 = end1+":"+end[1]
    pro1 = AuctedProduct.objects.get(product=pro)

    d = {'data': data,  'result': result,
         'pro': pro, 'pro1': pro1, 'end2': end2}

    return render(request, 'productdetail.html', d)


def StarAutction(request, pid):
    data = ''
    result = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    if data.membership.fee == "Unpaid":
        return redirect('wallet')

    pro4 = Product.objects.get(id=pid)
    end = pro4.session.time.split(':')
    end1 = ""
    if end[0] == "23":
        end1 = "00"
    else:
        end1 = str(int(end[0]) + 1)
    end2 = end1 + ":" + end[1]
    c = AuctedProduct.objects.get(product=pro4)
    pro1 = ""
    try:
        pro1 = Participant.objects.get(user=data, aucted_product=c)
    except:
        return redirect('allproduct')
    pro1 = Participant.objects.get(user=data, aucted_product=c)
    pro2 = Participant.objects.filter(aucted_product=c).order_by('-new_price')
    if request.method == "POST":
        p = request.POST["price"]
        pro1.new_price = p
        pro1.save()

    a = pro1.aucted_product.product.session.date.date
    li = a.split('-')
    total_time = (int(li[0]) * 365) + (int(li[1]) * 30) + (int(li[2]))
    d1 = datetime.date.today()
    d2 = datetime.datetime.now()
    c_time = d2.strftime("%H:%M")
    y = d1.year
    m = d1.month
    d = d1.day
    now_total = (int(y) * 365) + (int(m) * 30) + (int(d))
    li2 = pro1.aucted_product.product.session.time.split(':')
    li3 = c_time.split(':')
    time1 = (int(li2[0]) * 60) + int(li2[1])
    time2 = (int(li3[0]) * 60) + int(li3[1])
    time3 = time1 + 60
    terror = ""
    if total_time == now_total:
        if time1 == time2 or time2 < time3:
            pro1.aucted_product.product.temp = 2
            pro1.aucted_product.product.save()
        elif time2 > time3:
            pro1.aucted_product.product.temp = 3
            pro1.aucted_product.product.save()
            terror = "expire"
    elif total_time < now_total:
        pro1.aucted_product.product.temp = 3
        pro1.aucted_product.product.save()
        terror = "expire"
    win = Participant.objects.filter(aucted_product=c).order_by('-new_price')
    list1 = []
    for i in win:
        list1.append(i.id)
    win1 = Participant.objects.get(id=list1[0])
    if pro1.aucted_product.product.temp == 3:
        pro1.aucted_product.winner = win1.user.user.username
        pro1.aucted_product.save()
        for i in pro2:
            if i.user.user.username == pro1.aucted_product.winner:
                res = Result.objects.get(result="Winner")
                stat1 = Status.objects.get(status="Done")
                pay2 = Payment.objects.get(pay="pending")
                i.payment = pay2
                i.result = res
                i.aucted_product.product.status = stat1
                i.aucted_product.product.save()
                i.save()
            else:
                res1 = Result.objects.get(result="Defeat")
                pay1 = Payment.objects.get(pay="reject")
                i.payment = pay1
                i.result = res1
                i.save()

    d = {'data': data,  'result': result, 'pro': pro1,
         'pro2': pro2, 'end2': end2, 'terror': terror}
    return render(request, 'startauction.html', d)


def winner1(request, pid):
    data = ''
    result = ''
    user = User.objects.get(username=request.user.username)

    if (user):
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    else:
        user = User.objects.get(id=request.user.id)
        try:
            data = BidderUser.objects.get(user=user)
            if data:
                result = "bidder"
        except:
            data = AuctionUser.objects.get(user=user)
    if data.membership.fee == "Unpaid":
        return redirect('wallet')

    # pro2 = Product.objects.get(id=pid)
    # au = AuctedProduct.objects.get(product=pro2)
    # re = Result.objects.get(result="Winner")
    # pro1 = ""
    # try:
    #     pro1 = Participant.objects.get(aucted_product=au, result=re)
    # except:
    #     pass

    pro2 = Product.objects.get(id=pid)
    au = AuctedProduct.objects.get(product=pro2)
    re = Result.objects.get(result="Winner")
    pro1 = Participant.objects.get(aucted_product=au, result=re)

    d = {'data': data,  'result': result, 'pro': pro2, 'pro1': pro1}
    return render(request, 'winner1.html', d)
