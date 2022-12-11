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

    path('managerwallet', ManagerWallet, name="wallet"),
    path('addmoneytowallet', AddMoneyToWallet, name='addMoneyToWallet'),

    path('', Home, name="viewAuction"),
    path('', Home, name="biddingStatus"),
    path('', Home, name="addProduct"),
    path('', Home, name="allProduct"),
    path('', Home, name="biddingStatus2"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
