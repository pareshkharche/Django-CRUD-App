from django.shortcuts import render, redirect   
#from django.http import HttpResponse
from .models import Employee
# Create your views here.
def allemployees(request):
    emp = Employee.objects.all()
    return render(request, "emp/allemployees.html", {"allemployees" : emp})


def singleemployee(request, empid):
    return render(request, "emp/singleemployee.html")


def addemployee(request):
    if request.method == "POST":
        #take all the parameters from the form by there names kept
        employeeid       = request.POST.get('employeeid')
        employeename     = request.POST.get('employeename')
        employeeemail    = request.POST.get('employeeemail')

        employeeaddress  = request.POST.get('employeeaddress')
        employeephone    = request.POST.get('employeephone')

        #create an object of Employee model because  we have create the class of Employee in modesl.py file
        e = Employee()
        e.employeeid = employeeid
        e.employeename = employeename
        e.email = employeeemail
        e.address = employeeaddress
        e.phone = employeephone
        e.save()
        return redirect("/allemployees")
    return render(request, "emp/addemployee.html")


def deleteemployee(request, empid):
    e = Employee.objects.get(pk = empid)
    e.delete()
    return redirect("allemployees")

def updateemployee(request, empid):
    e = Employee.objects.get(pk = empid)
    #return redirect("allemployees")
    return render(request, "emp/updateemployee.html", {"singleemp" : e })

def doupdateemployee(request, empid):
    updateemployeeid      = request.POST.get('employeeid')
    updateemployeename    = request.POST.get('employeename')
    updateemployeeemail   = request.POST.get('employeeemail')
    updateemployeeaddress = request.POST.get('employeeaddress')
    updateemployeephone   = request.POST.get('employeephone')

    emp = Employee.objects.get(pk = empid)

    emp.employeeid  = updateemployeeid
    emp.employeename= updateemployeename
    emp.email       = updateemployeeemail
    emp.address     = updateemployeeaddress
    emp.phone       = updateemployeephone
    emp.save()

    return redirect("allemployees")  #here we can seee the updated values