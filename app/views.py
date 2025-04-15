from django.shortcuts import render , redirect , HttpResponse 
from .models import Accounts
from django.core.mail import send_mail
from django.conf import settings

import random
# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        aadhar = request.POST['aadhar']
        pan = request.POST['pan']
        mobile = request.POST['mobile']
        email = request.POST['email']
        address = request.POST['address']
        print("name,dob,mobile,aadhar,email,pan,address")
        Accounts.objects.create(name = name , DOB = dob, Aadhar = aadhar, pan = pan,
                                mobile = mobile , email = email, address = address   )
        #print("Successful")
        send_mail(f"hello {name},thank you for Creating an Accounts in our Bank ", 
        # subject
        f"FBH Fraud Bank Hydrabad ,\n Welcome to the Family of Our Bank " \
        "\n we are happy for it \n  , regards \n manager(DJD-E1)\n" \
        "thank you ****!" # body 
        ,settings.EMAIL_HOST_USER,[email],fail_silently = False          
        )
        print("sent Successfully")
    return render(request,'create.html')

def pin_gen(request):
    if request.method == "POST":
        otp = random.randint(100000,999999)
        acc = request.POST.get('acc')
        data = Accounts.objects.get(acc = acc)
        email = data.email
        send_mail(f"hello {data.name}",
        f"FBH Fraud Bank Hydrabad ,\nThe OTP (One Time Password) is {otp} " 
        "\n please share the otp only with our employees not for the outside scammers ,it is kind request \n  , regards \n manager(DJD-E1)\n" \
        "we Scam because we care" # body 
        ,settings.EMAIL_HOST_USER,[email],fail_silently = False  
        )
        print("sent Successfully")
        data.otp = otp
        data.save()
        return redirect("otp")
    return render(request,'pin.html')

def otp(request):
    if request.method == "POST":
        acc = request.POST['acc']
        otp = int(request.POST['otp'])
        pin1 = int(request.POST['pin1'])
        pin2 = int(request.POST['pin2'])
        if pin1 == pin2:
            data = Accounts.objects.get(acc = acc)
            if data.otp == otp:
                data.pin = pin2
                data.save()
                send_mail(f"hello {data.name} PIN GENERATION ",
                          
                f"FBH Fraud Bank Hydrabad ,\n we are happy to scam you " 
                "\n you have successfully generated the pin,we are happy to inforn that we know ur otp and"
                "Pin as well so we are happy to use ur money (ur money is our money and our money is our money) \n  ,"
                "regards \n manager(DJD-E1) \n we scam bcz we care " 
                 # body 
                ,settings.EMAIL_HOST_USER,[data.email],fail_silently = False  
                )
                print("sent Successfully")
            else:
                return HttpResponse("OTP mismatched")
        else:
            return HttpResponse("****** id not a valid pin u *****")
    return render(request,'valid_otp.html')

def balance(request):
    data = None
    msg = ""
    bal = 0
    f = False
    if request.method == "POST":
        acc = request.POST['acc']
        pin = request.POST['pin']
        try:
            data = Accounts.objects.get(acc = int(acc))
        except:
            # return HttpResponse("Enter the valid Accounts Number")
            # msg = "PLZ Enter the valid Accounts Number"
            pass
        if data is not None:
            if data.pin == int(pin):
                bal = data.bal
                f = True
            else:
                # return HttpResponse("Enter a valid pin")
                msg = "PLZ Enter the valid Pin"
        else:
            msg = "Plz Enter the Valid Accounts Number"
    context = {
        'bal' : bal,
        'var' : f,
        'msg' : msg
    }
    return render (request,'balance.html',context)

def withdraw(request):
    data = ""
    msg = ""
    bal = 0
    f = False
    if request.method == "POST":
        acc = request.POST['acc']
        pin = request.POST['pin']
        amt = int(request.POST.get('amt'))
        try:
            data = Accounts.objects.get(acc = acc)
        except:
            pass
        if data.pin == int(pin):
            if data.bal >= amt and amt > 0:
                data.bal -= amt
                data.save()
                send_mail(f"hello {data.name} WITHDRAWL ",
                          
                f"FBH Fraud Bank Hydrabad ,\n from ur {data.acc}  \n , {amt} has been" 
                f"withdrawled from the ATM the  Availabel Balance is {data.bal} \n ,"
                "regards \n manager(DJD-E1) \n we scam bcz we care " 
                 # body 
                ,settings.EMAIL_HOST_USER,[data.email],fail_silently = False  
                )
                print("sent Successfully")
                return redirect("home")
            else:
                msg = "Sorry ... Insufficient Balance"
        else:
            msg = "Incorrect Pin"
    context = {
        'bal' : bal,
        'var' : f,
        'msg' : msg
    }
        
    return render (request,'with.html',context)

def deposit(request):
    data = ""
    msg = ""
    bal = 0
    f = False
    if request.method == "POST":
        acc = request.POST['acc']
        pin = request.POST['pin']
        amt = int(request.POST.get('amt'))
        try:
            data = Accounts.objects.get(acc = acc)
        except:
            pass
        if data.pin == int(pin):
            if amt >= 100 and amt <= 10000:
                data.bal += amt
                data.save()
                send_mail(f"hello {data.name} WITHDRAWL ",
                          
                f"FBH Fraud Bank Hydrabad ,\n from ur {data.acc}  \n , {amt} as be" 
                f"deposited to ur acc {data.acc} Balance is {data.bal} \n ,"
                "regards \n manager(DJD-E1) \n we scam bcz we care " 
                 # body 
                ,settings.EMAIL_HOST_USER,[data.email],fail_silently = False  
                )
                print("sent Successfully")
                return redirect("home")
            else:
                msg = "Sorry ... Insufficient Balance"
        else:
            msg = "Incorrect Pin"
    context = {
        'bal' : bal,
        'var' : f,
        'msg' : msg
    }
        
    return render (request,'deposit.html',context)

def transfer(request):
    msg = ""
    if request.method =="POST":
        f_acc = request.POST.get('f_acc')
        t_acc = request.POST.get('t_acc')
        pin = request.POST.get('pin')
        amt = request.POST.get('amount')
        print(f_acc,t_acc,pin,amt)
        try:
            from_acc = Accounts.objects.get(acc = f_acc)
            print(from_acc.name)
        except:
            msg = "senders Accounts  number is not valid"
            print(msg)
        try:
            to_acc = Accounts.objects.get(acc = t_acc)
        except:
            msg = "receiver Accounts is not valid"
            
        if from_acc.pin == int(pin):
            if int(amt) >= 100 and int(amt) <= 10000 and int(amt) <= from_acc.bal:
                from_acc.bal -= int(amt)
                from_acc.save()
                send_mail(f"hello {from_acc.name} Accounts TRANSFER ",         
                f"FBH Fraud Bank Hydrabad ,\n from ur {from_acc.acc}  \n , {amt} has be" 
                f"debited to {to_acc.acc} Accounts Balance is {from_acc.bal} \n ,"
                "regards \n manager(DJD-E1) \n we scam bcz we care " 
                 # body 
                ,settings.EMAIL_HOST_USER,[from_acc.email],fail_silently = False  
                )
                print("sent Successfully")
                to_acc.bal += int(amt)
                to_acc.save()
                send_mail(f"hello {to_acc.name} Accounts TRANSFER ",         
                f"FBH Fraud Bank Hydrabad ,\n from ur {to_acc.acc}  \n , {amt} has been" 
                f"credited from {from_acc.acc} Accounts Balance is {to_acc.bal} \n ,"
                "regards \n manager(DJD-E1) \n we scam bcz we care " 
                 # body 
                ,settings.EMAIL_HOST_USER,[to_acc.email],fail_silently = False  
                )
                print("sent Successfully")
            else:
                msg = "Enter the Valid Amount"
        else:
            msg = "Incorrect Pin"
                
    return render(request,'transfer.html',{'msg':msg})