"""amazon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from aboutUs.views import aboutus
from affairs.views import register, loginFun, home, delete, logoutST, InsertIntake, IntakesList
from contactUs.views import contactus
from home.views import greeting


urlpatterns = [
    path('admin/', admin.site.urls),
    path('/<name>', greeting),
    path('home/', home),
    path('contactus', contactus),
    path('aboutus', aboutus),
    path('register/', register),
    path('login/', loginFun),
    path('delete/<int:selectST>/', delete, name="delete"),
    path('logout/', logoutST),
    path('insertintake/', InsertIntake.as_view(), name="insertIntake"),
    path('listintake/', IntakesList.as_view(), name="IntakeList"),
]
