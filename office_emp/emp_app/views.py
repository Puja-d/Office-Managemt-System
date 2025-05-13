from django.shortcuts import render,HttpResponse,redirect
from emp_app.models import *
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context= {
        'emps':emps
    }
    print(context)
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonous=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonous=bonous,phone=phone,dept_id = dept,role_id = role,hire_date=datetime.now())
        new_emp.save()
        # return HttpResponse('added employee')
        return redirect('all_emp')
    elif request.method=='GET':
         return render(request,'add_emp.html')
    else:
      return HttpResponse('exception')

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_removed=Employee.objects.get(id=emp_id)
            emp_to_removed.delete()
            return HttpResponse('employee removed')
        except:
            return HttpResponse('please enter a valid employee id')
            
            
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps=emps.filter(dept__name__icontains = dept)  
        if role:
            emps=emps.filter(role__name__icontains = role)  
        context={
            'emps':emps
        }
        return render(request,'all_emp.html',context)
        
    elif request.method=='GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('error')
    
@login_required(login_url='/login/')    
def logout_view(request):
    logout(request)
    return redirect('login') 
@login_required(login_url='/login/')
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        return redirect('login')
    elif request.method=='GET':
        return render(request,'signup.html')
    else:
        return HttpResponse('error')
@login_required(login_url='/login/')    
def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse('invalid credentials')
    elif request.method=='GET':
        return render(request,'login.html')
    else:
        return HttpResponse('error')
    
