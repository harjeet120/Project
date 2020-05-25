from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from addition.models import bookings
from day2.models import packagedetails
from python import checksum

MERCHANT_KEY = "tdbDZejvDaBtvK3O"

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def page(request):
    return render(request,'page.html')

def register(request):
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['username']
        em = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1==pass2:
            if User.objects.filter(username=un).exists():
                messages.info(request,'Username Taken')

            elif User.objects.filter(email=em).exists():
                messages.info(request,'Email Taken')

            else:
                user = User.objects.create_user(username=un, email=em, first_name=fn, password=pass1, last_name=ln)
                user.save()
                print('user created')
        else:
            messages.info(request,'password not matched!')
            return redirect('register')
        return redirect('places')
    else:
        return render(request,'register.html')

def detail(request):
    y = packagedetails.objects.all()
    return render(request,'detail.html',{'y': y})

def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']

        user = auth.authenticate(username=un, password=pw)

        if user is not None:
            auth.login(request, user)
            return redirect('places.html')
        else:
            messages.info(request, 'Invalid credentials!')
            return redirect('places')
    else:
        return render(request,'login.html')




def places(request):
    return render(request, 'places.html')

def booking(request,package_id):
    if request.method == 'POST':
        un = request.POST['username']
        noa = request.POST['no_of_adults']
        noc = request.POST['no_of_childrens']
        nor = request.POST['no_of_rooms']
        wfm = request.POST['want_for_meal']
        motcf = request.POST['mode_of_travel_car_flight']
        dd = request.POST['departure_date']
        ad = request.POST['arrival_date']
        pn = request.POST['phone_number']
        ct = request.POST['city']

        user = User.objects.create_user(username=un)
        data = bookings(no_of_adults=noa, no_of_childrens=noc, no_of_rooms=nor, want_for_meal=wfm, mode_of_travel_car_flight=motcf,
               departure_date=dd, arrival_date=ad, phone_number=pn, city=ct)
        user.save()
        data.save()
    x = packagedetails.objects.all()
    y = packagedetails.objects.get(PackageID = package_id)
    return render(request,'booking.html',{'x': x,'y':y})



def paymentMode(request,pk):
    h=packagedetails.objects.get(pk=pk)

    param_dict = {
        "MID": "qDcIfS32196519134847",
        "ORDER_ID": "450",
        "CUST_ID": "101",
        "TXN_AMOUNT": str(h.FoodCharge),
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "WEBSTAGING",
        #"CALLBACK_URL": "http/127.0.0.1:8000/handleRequest/",
        "CALLBACK_URL":"https://merchant.com/callback/"

    }
    param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict,MERCHANT_KEY)

    return render(request,'paytm.html',{'params':param_dict})

@csrf_exempt
def handlerequest(request):
    #paytm will send you post request here
    return redirect('/Thanks')