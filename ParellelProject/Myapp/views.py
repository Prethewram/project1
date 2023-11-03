from django.shortcuts import render,redirect
from Myapp.models import shopdb,productdb,contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages
# Create your views here.

def mypage(req):
    return render(req,"indexx.html")

def category(req):
    return render(req,"addcat.html")


def savedata(req):
    if req.method == "POST":
        na = req.POST.get('name')
        ds = req.POST.get('des')
        img = req.FILES['image']
        obj = shopdb(CName=na,CDes=ds,Cimage=img)
        obj.save()
        messages.success(req,"category saved successfully...")
        return redirect(category)

def disdata(req):
    data = shopdb.objects.all()
    return render(req,"display.html",{'data':data})

def editcat(req,dataid):
    cat=shopdb.objects.get(id=dataid)
    return render(req,"editcat.html",{'cat':cat})

def deletecat(req,dataid):
    dele = shopdb.objects.filter(id=dataid)
    dele.delete()
    messages.error(req, "category deleted successfully...")
    return redirect(disdata)

def updatedata(req,dataid):
    if req.method == "POST":
        cn = req.POST.get('name')
        cd = req.POST.get('des')
        try:
            cimg = req.FILES['image']
            fs = FileSystemStorage()
            files = fs.save(cimg.name,cimg)
        except MultiValueDictKeyError:
            files=shopdb.objects.get(id=dataid).Cimage
            shopdb.objects.filter(id=dataid).update(CName=cn,CDes=cd,Cimage=files)
            messages.success(req, "category updated successfully...")
            return redirect(disdata)


def addproduct(req):
    cat = shopdb.objects.all()
    return render(req,"Addproduct.html",{'cat':cat})

def saveproduct(req):
    if req.method == "POST":
        nam =req.POST.get('cname')
        pna =req.POST.get('name')
        de =req.POST.get('des')
        pri =req.POST.get('price')
        img =req.FILES['image']
        obj = productdb(Catname=nam,Productname=pna,Description=de,Price=pri,Image=img)
        obj.save()
        return redirect(addproduct)

def adminlogin(req):
    return render(req,"adminlog.html")

def displayproduct(req):
    data=productdb.objects.all()
    return render(req,"dispro.html",{'data':data})

def editproduct(req,dataid):
    ed=shopdb.objects.all()
    pro = productdb.objects.get(id=dataid)
    return render(req,"editpro.html",{'ed':ed ,'pro': pro})

def deleteproduct(req,dataid):
    dlt = productdb.objects.filter(id=dataid)
    dlt.delete()
    return redirect(displayproduct)

def updateproduct(req,dataid):
    if req.method == "POST":
        cn = req.POST.get('cname')
        pn = req.POST.get('name')
        de = req.POST.get('des')
        pr = req.POST.get('price')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Catname=cn,Productname=pn,Description=de,Price=pr,Image=file)
        return redirect(displayproduct)

def adminlogin(request):
    return render(request,"adminlog.html")

def admlog(request):
    if request.method =="POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')

        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pwd)
            if user is not None:
             login(request,user)
             request.session['username']=un
             request.session['password']=pwd
             return redirect(mypage)
            else:
                return redirect(adminlogin)
        else:
             return redirect(adminlogin)


def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)

def displaycontact(request):
    disp =contactdb.objects.all()
    return render(request,"displaycontact.html",{'disp':disp})


