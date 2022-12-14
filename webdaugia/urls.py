"""webdaugia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from daugia.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name="home"),
    path('login/', LoginUser, name="loginUser"),
    path('register/', Register, name="registerUser"),
    path('logout', Logout, name="logout"),
    path('profileuser/', ProfileUser, name="profileUser"),
    path('editrofileuser/', EditProfileUser, name="editProfileUser"),
    path('changepassword', ChangePassword, name="changePassword"),

    # /////////////////////////////////

    path('managerwallet', ManagerWallet, name="wallet"),
    path('addmoneytowallet', AddMoneyToWallet, name='addMoneyToWallet'),

    # /////////////////////////////////

    path('dashboard', AdminHome, name="adminHome"),

    path('adminaddsectiondate', AdminAddSeactionDate, name="adminaddsectiondate"),
    path('editsessiondate(<int:pid>)',
         EditSessiondate, name='editsessiondate'),
    path('deletesessiondate(<int:pid>)',
         Deletesessiondate, name='deletesessiondate'),
    path('adminviewsectiondate', AdminViewSeactionDate,
         name="adminviewsectiondate"),

    path('adminaddsectiontime', AdminAddSeactionTime, name="adminaddsectiontime"),
    path('editsessiontime(<int:pid>)',
         EditSessionTime, name='editsessiontime'),
    path('deletesessiontime(<int:pid>)',
         DeletesessionTime, name='deletesessiontime'),
    path('adminviewsectiontime', AdminViewSeactionTime,
         name="adminviewsectiontime"),



    path('adminaddcategory', AdminAddCategory, name="adminaddcategory"),
    path('editcategory(<int:pid>)', EditCategory, name='editcategory'),
    path('deletecategory(<int:pid>)', DeleteCategory, name='deletecategory'),
    path('adminviewcategory', AdminViewCategory, name="adminviewcategory"),


    path('adminaddsubcategory', AdminAddSubcategory, name="adminaddsubcategory"),
    path('editsubcategory(<int:pid>)',
         EditSubCategory, name='editsubcategory'),
    path('deletesubcategory(<int:pid>)',
         DeleteSubCategory, name='deletesubcategory'),
    path('adminviewsubcategory', AdminViewSubcategory,
         name="adminviewsubcategory"),

    path('adminaddproducionverification', AdminAddProducionVerification,
         name="adminaddproducionverification"),
    path('adminviewproducionverification', AdminViewProducionVerification,
         name="adminviewproducionverification"),

    path('adminbidderuser', AdminBidderUserManager, name="adminbidderuser"),
    path('adminselleruser', AdminSellerUserManager, name="adminselleruser"),

    path('adminresult', AdminResult, name="adminresult"),
    path('adminfeedBack', AdminFeedBack, name="adminfeedBack"),

    # /////////////////////////////////
    path('addproduct', AddProduct, name="addProduct"),
    path('loadcourses/', LoadCourses, name='ajaxloadcourses'),
    path('loadcourses1/', LoadCourses1, name='ajaxloadcourses1'),
    path('productdetail2(<int:pid>)', ProductDetail2, name='productdetail2'),
    path('status(<int:pid>)', ChangeStatus, name='status'),


    # /////////////////////////////////
    path('allproduct', AllProduct, name="allproduct"),
    path('apiauctionuserallproduct(<int:pid>)', ApiParticipateduser,
         name="allproduapiauctionuserallproductct"),

    path('particpateduser(<int:pid>)',
         ParticipatedUser, name='particpateduser'),
    path('biddingstatus2', BiddingStatus2, name='biddingstatus2'),

    # /////////////////////////////////
    #     acctor
    path('viewauction', ViewAuction, name='viewauction'),
    path('viewauction(<int:pid>)', ViewAuction1, name='viewauction1'),
    path('startauction(<int:pid>)', StarAutction, name='startauction'),
    path('winner1(<int:pid>)', winner1, name='winner1'),
    path('productdetail(<int:pid>)', productdetail, name='productdetail'),

    path('bidding_status', BiddingStatus, name='bidding_status'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
