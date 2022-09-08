from django.shortcuts import render
from crud_login.forms import NewUserForm, UserCreationForm
from crud_login.models import Employee


def index(request):
    return render(request, 'crud_login/index.html')


def create(request):
    if request.method == "POST":
        var = request.POST.get('a')
        var1 = request.POST.get('b')
        employee = Employee(emp_id=var, emp_contact=var1)
        employee.save()
    return render(request, 'crud_login/create.html')


def read(request):
    employees = Employee.objects.all()
    return render(request, 'crud_login/read.html', {'employees': employees})


def update_record(request, id):
    if request.method == "POST":
        var1 = request.POST.get('a')
        var2 = request.POST.get('b')
        employee = Employee.objects.get(id=id)
        employee.emp_id = var1
        employee.emp_contact = var2
        employee.save()
        return render(request, 'crud_login/read.html')


def update(request):
    return render(request, 'crud_login/update.html')


def delete(request):

    return render(request, "crud_login/read.html")


def register(request):
    return render(request, "crud_login/register.html", {'NewUserForm': NewUserForm})


def login(request):
    return render(request, 'crud_login/login.html', )


def logout(request):
    return render(request, 'crud_login/logout.html')


def func(request):
    return render(request, 'crud_login/create.html')


def forgot(request):
    return render(request, 'crud_login/forgot.html')


def delete_record(request,id):
    if request.method=="POST":
        var=id
        employee=Employee.objects.get(id=var)
        employee.delete()
    return render(request,'crud_login/read.html')


