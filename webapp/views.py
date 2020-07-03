from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django.contrib import messages
from . import utils
from .models import Employee
import json

# render request to login page
def login(request):
    return render(request,'login.html')

# render request to listing page with employee json obj
def list(request):

    if request.method == 'POST':
        

        employee1 = Employee('emp1234','Albus Dumbledore','dumbledorealbus@wizard.com','19-10-2012','Bradford')
        employee2 = Employee('emp5678','Severus Snape','severussnape@wizard.com','17-03-2012','Belfast')
        employee3 = Employee('emp9012','Rubeus Hagrid','hagridrubeus@wizard.com','08-06-2012','Carlisle')
        employee4 = Employee('emp3456','Sirius Black','blacksirius@wizard.com','07-02-2012','Lancaster')
        employee5 = Employee('emp7890','Mad-Eye Moody','madeyemoody@wizard.com','24-09-2012','Manchester')
        employee6 = Employee('emp0125','Tom Riddle','tomriddle@wizard.com','15-04-2012','Norwich')

        emp_list = [employee1, employee2, employee3, employee4, employee5, employee6]

        #list of obj to json
        list_json = json.dumps(emp_list, default = lambda x: x.__dict__)

        if 'email' in request.POST and 'password' in request.POST :
            email = request.POST.get('email').strip()
            password = request.POST.get('password')
            if email == 'admin@mail.com' and password == '123':
                return render(request,'list.html',{'list_json':list_json,'user':email})
            else:
                print('Invalid credentials')
                messages.info(request,'Invalid credentials')
                return redirect('/')
                
        elif 'flag' in request.POST:
            email = request.POST.get('email')
            return render(request,'list.html',{'list_json':list_json,'user':email})
    else:
        print("Not a POST request")
        return render(request,'error.html')

# render request to detail page
def detail(request):
    print(request.POST.get)
    id = request.POST.get('id')
    ename = request.POST.get('ename')
    email_id = request.POST.get('email_id')
    joining_date = request.POST.get('joining_date')
    location = request.POST.get('location')
    user = request.POST.get('user')

    employee = Employee(id, ename, email_id, joining_date, location)
    return render(request,'detail.html',{'employee':employee,'user':user})
    
    #return render(request,'list.html')



    