import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','student.settings')

import django
django.setup()
from app.models import *

import random
from faker import Faker
f=Faker()
admins=['narayana','vagdevi','srisai','chaithanya','littles','angiles','kesavareddy','faith']

def add_admin():
    admin_name=random.choice(admins)
    t=Admin.objects.get_or_create(admin_name=admin_name)[0]
    t.save()
    return t
def add_teacher(teachername,url):
    t=add_admin()
    w=Teacher.objects.get_or_create(admin_name=t,name=teachername,url=url)[0]
    w.save()
    return w

def add_student(teachername,url,date):
    name=add_teacher(teachername,url)
    a=Student.objects.get_or_create(name=name,date=date)[0]
    a.save()

def add_data(n):
    for i in range(n):
        fake_name=f.first_name()
        fake_url=f.url()
        fake_date=f.date()


        add_student(fake_name,fake_url,fake_date)


if __name__=='__main__':

    n=int(input('enter n value'))
    print('population is started')
    add_data(n)
    print('population is  done successfully')



