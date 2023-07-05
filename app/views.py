from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def deprt(request):
    if request.method=="POST":
        dn=request.POST['dn']
        dname=request.POST['dname']
        loc=request.POST['loc']
        DN=Dept.objects.get_or_create(deptno=dn,dname=dname,loc=loc)[0]
        DN.save()
        return HttpResponse("Inserted Successfully")
    return render(request,'Dept.html')
def employ(request):
    LDO=Dept.objects.all() # inheriting department table to employee table
    d={'LDO':LDO} #jinja syntax
    if request.method=="POST":
        dn=request.POST['deptno']
        eno=request.POST['e']
        en=request.POST['ename']
        job=request.POST['job']
        mgr=request.POST['mgr']
        hiredate=request.POST['hiredate']
        sal=request.POST['sal']
        comm=request.POST['comm']
        DN=Dept.objects.get(deptno=dn)
        emp=Emp.objects.get_or_create(deptno=DN,empno=eno,ename=en,job=job,mgr=mgr,hiredate=hiredate,sal=sal,comm=comm)[0]
        emp.save()
        return HttpResponse("Inserted Successfully")
    return render(request,'Emp.html',d)


