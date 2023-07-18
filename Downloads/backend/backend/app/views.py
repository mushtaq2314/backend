from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from ast import literal_eval as le
from .models import orders,customizations
global item
global uname
dict = {}
dict2 = {}
occasion = ''
price = ''
skintone = ''
def index(request):
    return render(request,'index.html')
def shirts(request):
    if request.method == 'POST':
        global item
        item = request.POST.get('item')
        item+=' -Shirt'
        print(item)
        return redirect('/individual_item_layout')
    return render(request,'SHIRTS.html')
def pants(request):
    if request.method == 'POST':
        global item
        item = request.POST.get('item')
        item+=' -Pants'
        print(item)
        return redirect('/individual_item_layout2')
    return render(request,'pants.html')
def kurtas(request):
    if request.method == 'POST':
        global item
        item = request.POST.get('item')
        item+=' -Kurta'
        print(item)
        return redirect('/individual_item_layout')
    return render(request,'KURTAS.html')
def rental(request):
    return render(request,'rental.html')

def shopnow(request):
    return render(request, 'SHOP NOW.html')

def contact(request):
    return render(request,'CONTACT_US.html')
def customization_front(request):
    return render(request,'customization_front.html')
def customization(request):
    return render(request,'customization.html')
def customization2(request):
    global occasion
    global skintone
    global price
    if request.method == 'POST':
        occasion = request.POST.get('occasion')
        price = request.POST.get('price')
        skintone = request.POST.get('skin')
        dict2.update({"Chest":request.POST.get('chestsize')})
        dict2.update({"Neck":request.POST.get('necksize')})
        dict2.update({"Cuff":request.POST.get('cuffsize')})
        dict2.update({"Length":request.POST.get('length')})
        dict2.update({"Instruction1":request.POST.get('instruction')})
        dict2.update({"Waist":request.POST.get('waist')})
        dict2.update({"Bottom":request.POST.get('bottom')})
        dict2.update({"Length":request.POST.get('length2')})
        dict2.update({"Instruction2":request.POST.get('instruction2')})
        print(dict2)
        print(occasion)
        return redirect('/user2')
    return render(request,'customization2.html')
def individual_item_layout(request):
    if request.method == 'POST':
        dict.update({"Chest":request.POST.get('chestsize')})
        dict.update({"Neck":request.POST.get('necksize')})
        dict.update({"Cuff":request.POST.get('cuffsize')})
        dict.update({"Length":request.POST.get('length')})
        dict.update({"Instruction":request.POST.get('instruction')})
        print(item)
        print(dict)
        return redirect('/user')
    else:
        return render(request,'individual_item_layout.html')
def individual_item_layout2(request):
    if request.method == 'POST':
        dict.update({"Waist":request.POST.get('waist')})
        dict.update({"Bottom":request.POST.get('bottom')})
        dict.update({"Length":request.POST.get('length')})
        dict.update({"Instruction":request.POST.get('instruction')})
        return redirect('/user')
    return render(request,'individual_item_layout2.html')
def user(request):
    return render(request,'user.html')
def user2(request):
    return render(request,'user2.html')
def buy(request):
    print(item)
    print(dict)
    print(uname)
    if(request.user.is_anonymous):
        return render(request,'user.html',{'msg':'Please login first!'})
    if(request.method=='POST'):
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        print("FIRST and LAST names",firstname,lastname)
        x= item
        y = str(dict)
        order = orders(username=uname,
            item=x,
            size = y,
            firstname=request.POST.get('fname'),
            lastname=request.POST.get('lname'),
            email=request.POST.get('email'),
            country=request.POST.get('country'),
            address=request.POST.get('address'),
            state=request.POST.get('state'),
            city=request.POST.get('city'),
            pincode=request.POST.get('pincode'),
            method=request.POST.get('method'),
        )
        order.save()
        
    return render(request,'BUYPAGE.html')
def buy2(request):
    global occasion
    global skintone
    global price
    print(dict2)
    print(uname)
    if(request.user.is_anonymous):
        return render(request,'user.html',{'msg':'Please login first!'})
    if(request.method=='POST'):
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        print("FIRST and LAST names",firstname,lastname)
        x= 0
        y = str(dict2)
        order = customizations(username=uname,
            occasion=occasion,
            pricerange=price,
            skintone=skintone,
            dimensions=y,
            firstname=request.POST.get('fname'),
            lastname=request.POST.get('lname'),
            email=request.POST.get('email'),
            country=request.POST.get('country'),
            address=request.POST.get('address'),
            state=request.POST.get('state'),
            city=request.POST.get('city'),
            pincode=request.POST.get('pincode'),
            method=request.POST.get('method'),
        )
        order.save()
        
    return render(request,'BUYPAGE2.html')

def signupUser(request):
    if(request.method=='POST'):
        try:
            global uname
            uname= request.POST.get('signup-username')
            pwd= request.POST.get('signup-password')
            user=User.objects.create_user(username=uname,password=pwd)
            user.save()
            print(uname,pwd)
            return render(request,'BUYPAGE.html')
        except Exception as e:
            if(str(e)=='UNIQUE constraint failed: auth_user.username'):
                return render(request,'user.html',{'msg':'Username Already Taken!'})
    return render(request,'user.html')

def loginUser(request):
    if(request.method=='POST'):
        global uname
        uname = request.POST.get('login-username')
        pwd = request.POST.get('login-password')
        print(uname,pwd)
        user= authenticate(username=uname,password=pwd)
        if(user is not None):
            login(request,user)
            return render(request,'BUYPAGE.html',{'name':uname})
        else:
            return render(request,'user.html',{'msg':'Invalid Credentials!'})
    return render(request,'user.html')
def signupUser2(request):
    if(request.method=='POST'):
        try:
            global uname
            uname= request.POST.get('signup-username')
            pwd= request.POST.get('signup-password')
            user=User.objects.create_user(username=uname,password=pwd)
            user.save()
            print(uname,pwd)
            return render(request,'BUYPAGE2.html')
        except Exception as e:
            if(str(e)=='UNIQUE constraint failed: auth_user.username'):
                return render(request,'user2.html',{'msg':'Username Already Taken!'})
    return render(request,'user2.html')

def loginUser2(request):
    if(request.method=='POST'):
        global uname
        uname = request.POST.get('login-username')
        pwd = request.POST.get('login-password')
        print(uname,pwd)
        user= authenticate(username=uname,password=pwd)
        if(user is not None):
            login(request,user)
            return render(request,'BUYPAGE2.html',{'name':uname})
        else:
            return render(request,'user2.html',{'msg':'Invalid Credentials!'})
    return render(request,'user2.html')