from django.shortcuts import render

# Create your views here.
from app.models import *
def dis_admin(request):
    admins=Admin.objects.all()
    d={'admins':admins}
    return render(request,'dis_admin.html',context=d)

def dis_teacher(request):
    teachers=Teacher.objects.all()
    e={'teachers':teachers}
    return render(request,'dis_teacher.html',context=e)

def dis_student(request):
    students=Student.objects.all()
    ve={'students':students}
    return render(request,'dis_student.html',context=ve)
