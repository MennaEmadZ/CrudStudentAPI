from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import students, Intake
from .forms import Intakeform
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(req):
    context = {}
    context['students'] = students.objects.all()
    if (req.method == 'GET'):
        return render(req, 'home.html', context)


def register(request):
    context={}
    if(request.method == 'GET'):
        return render(request,'Register.html')
    else:
        students.objects.create(username=request.POST.get('username'), password = request.POST.get('password') )
        User.objects.create(username=request.POST.get('username'), password=request.POST.get('password'))
        context['users'] = students.objects.all()
        return render(request,'Login.html',context)

def loginFun(request):
    context={}
    if (request.method=='GET'):
        return render(request,'Login.html')
    else:

        lgAuth=authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        lgST=students.objects.filter(username=request.POST.get('username'), password=request.POST.get('password'))
        print(lgAuth)
        print(lgST)
        if(lgST and lgAuth):
            login(request,lgAuth)
            return HttpResponseRedirect('/home')
        else:
           print("entered else")
           context['error'] = 'password or email not valid'
           return render(request, 'Login.html', context)


def delete(request,selectST):

    obj = students.objects.get( id = selectST)
    obj.delete()

    return HttpResponseRedirect('/home')


def logoutST(request):
    logout(request)
    return HttpResponseRedirect('/login')


class InsertIntake(View):
    def get(self, req):
        context = {}
        form = Intakeform()
        if (req.method == 'GET'):
            context['form'] = form
            return render(req, 'Intake.html', context)

    def post(self, req):
        Intake.objects.create(intakeName=req.POST['intakeName'], startDate=req.POST['startDate'],
                              endDate=req.POST['endDate'])

        return HttpResponseRedirect('/home')

class IntakesList(ListView):
    model=Intake