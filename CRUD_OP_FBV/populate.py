import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CRUD_OP_FBV.settings')
import django
django.setup()



from testapp.models import Employee
from faker import Faker
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randint(15000,35000)
        feaddr=faker.city()
        emp_record=Employee.objects.get_or_create(
            eno=feno,ename=fename,esal=fesal
            ,eaddr=feaddr )
n= int(input("Enter number of employee you want:"))
populate(n)
print("{} Record inserted SuccessFully....".format(n))
