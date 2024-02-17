from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')

def student(request):
    name=request.session['name']
    return render(request, 'student.html',{'name':name})
def staff(request):
    name=request.session['name'] 
    return render(request, 'staff.html',{'name':name})
def admin(request):
    name=request.session['name']
    return render(request, 'admin.html',{'name':name})
def editor(request):
    name=request.session['name']
    return render(request, 'editor.html',{'name':name})

def register(request):
    if request.method == 'POST':
        
        name = request.POST['name']
        email = request.POST['email']
        role = request.POST['role'] 
        country = request.POST['country']
        nationality = request.POST['nationality']
        mobile = request.POST['mobile']
        password = request.POST['password']
        reg=Registeration(name=name,email=email,role=role,country=country,nationality=nationality,
        mobile=mobile,password=password)
        reg.save()
        
        return redirect('login')  
    else:
       
        # messages.info(request,"All fields are required")
        return render(request, 'register.html')

def signin(request):
    print("login.......")
    if request.method == 'POST':
        
        email = request.POST['email'] 
        password = request.POST['password']
        user = Registeration.objects.all().filter(email=email, password=password)
        if user:
            for x in user:
                email=x.email
                password=x.password
                role=x.role
                name=x.name
               
                request.session['lid']=x.id
                request.session['role']=role
                request.session['name']=name

                
                if email == email and password==password and role=="student":
                    
                    
                    return HttpResponseRedirect('student')
                elif email == email and password==password and role=="staff":
                    
                    
                    return HttpResponseRedirect('staff')
                elif email == email and password==password and role=="admin":
                    
                    
                    return HttpResponseRedirect('admin')
                elif email == email and password==password and role=="editor":
                    
                    
                    return HttpResponseRedirect('editor')
               
               
                else:
                    messages.error(request, 'invalid Username or Passwords')		
                    return render(request,'login.html')
        else:
            messages.error(request, 'invalid Username or Passwords')		
            return HttpResponseRedirect('login')
    else:
        
        return render(request,'login.html')       


def logout(request):
	try:
		 del  request.session['id']
	except KeyError:
		pass
	return HttpResponseRedirect('login')