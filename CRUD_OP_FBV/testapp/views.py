from django.shortcuts import render,redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm

def retrive_view(request):
    emp_list=Employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})
def inser_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/insert.html',{'form':form})


def delete(request,id):
    Emp=Employee.objects.get(id=id)
    Emp.delete()
    return redirect('/')
def update_view(request,id):
    emp=Employee.objects.get(id=id)
    form=EmployeeForm(instance=emp)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/update.html',{'form':form})