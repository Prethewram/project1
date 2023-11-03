from django.shortcuts import render,redirect
from Myapp.models import shopdb,productdb,contactdb
from webapp.models import registerdb1,cartdb

# Create your views here.

def homepage(req):
    cat=shopdb.objects.all()
    return render(req,"home.html", {'cat':cat})

def product_page(req):
    pro = productdb.objects.all()
    return render(req,"product.html",{'pro':pro})

def single_product(req,prodid):
    data=productdb.objects.get(id=prodid)
    return render(req,"single_product.html",{'data':data})

def filtered_product(request,cat_name):
    data=productdb.objects.filter(Catname=cat_name)
    return render(request,"filtered_product.html",{'data':data})

def aboutpage(request):
    return render(request,"aboutpage.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")

def savecontact(request):
    if request.method == "POST":
        fn=request.POST.get('first_name')
        ln=request.POST.get('last_name')
        em=request.POST.get('email')
        ad=request.POST.get('address')
        ci=request.POST.get('city')
        zc=request.POST.get('zip_code')
        mo=request.POST.get('mob')
        obj=contactdb(Firstname=fn,Lastname=ln,Email=em,Address=ad,City=ci,Zipcode=zc,Mobile=mo)
        obj.save()
        return redirect(contact)

def registration_page(request):
    return render(request,"LOGIN.html")

def registerdata(request):
    if request.method == "POST":
        rn = request.POST.get('name')
        rm = request.POST.get('number')
        re = request.POST.get('email')
        ra = request.POST.get('address')
        ru = request.POST.get('username')
        rp = request.POST.get('password')
        obj = registerdb1(Name=rn,Mobile=rm,Email=re,Address=ra,Username=ru,Password=rp)
        obj.save()
        return redirect(registration_page)

def userlogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if registerdb1.objects.filter(Username=un,Password=pwd).exists():
            request.session['Username'] = un
            request.session['Password'] = pwd
            return redirect(homepage)
        else:
            return redirect(registration_page)
    return redirect(registration_page)

def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(registration_page)

def cartpage(request):
    data= cartdb.objects.filter(Username=request.session['Username'])
    Total_prize=0
    for d in data:
        Total_prize=Total_prize+d.Totalprize
    return render(request,"cartpage.html",{'data':data,'Total_prize':Total_prize})

def savecartpage(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pn = request.POST.get('productname')
        de = request.POST.get('description')
        qn = request.POST.get('quantity')
        tp = request.POST.get('totalprice')
        obj = cartdb(Username=un,Productname=pn,Description=de,Quantity=qn,Totalprize=tp)
        obj.save()
        return redirect(cartpage)

def delete_pro(request,dataid):
    deletee = cartdb.objects.filter(id=dataid)
    deletee.delete()
    return redirect(cartpage)

def Checkout_page(request):
    data = cartdb.objects.all()
    check = cartdb.objects.filter(Username=request.session['Username'])
    Total = 0
    for i in check:
        Total = Total + i.Totalprize
    return render(request,"Checkout.html",{'data':data ,'check':check ,'Total':Total})

def checkoutsummary(request):
    return render(request,"checkoutpage.html")
