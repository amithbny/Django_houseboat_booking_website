from django.shortcuts import render,redirect
from django.utils import timezone
from  .models import Heading,Slide,HouseBoat,Package,Menu,Profile,BoatBooking
from .forms import Regform,Update,BookingRegister
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.

# Home Page

def home(request):
    content = Slide.objects.all()
    return render(request, 'main.html',{'content':content})

# houseboat Page Showing All Houseboats

def houseboats(request):
    empty = ''
    if request.GET.get('srch'):
        empty=request.GET.get('srch')
        hb = HouseBoat.objects.filter(title__icontains=empty)
        return render(request, 'houseboat.html',{'boats':hb}) 
    else:
        boats = HouseBoat.objects.all()
        return render(request, 'houseboat.html',{'boats':boats})

# Packages Available 

def packages(request):
    empty = ''
    if request.GET.get('srch'):
        empty=request.GET.get('srch')
        hb = Package.objects.filter(title__icontains=empty)
        return render(request, 'package.html',{'package':hb}) 
    else:
        package = Package.objects.all()
        return render(request, 'package.html', {'package':package})

# Detail Page for Packages

def package_detail_pg(request,id):
    package_detail_pg = Package.objects.get(id=id)
    return render(request, 'detail.html', {'detail_pg':package_detail_pg})


# tariff

def tariff(request):
    menu_detail= Menu.objects.all()
    return render(request,'menu_detail.html',{'menu_detail':menu_detail})

# Creating a user

def regForm(request):
    if request.method=='POST':
        form = Regform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User has been Created')
            return render(request,'messages.html')
    else:
        form = Regform()
    return render(request,'register.html',{'form':form})

# Profile Page
@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    booking = BoatBooking.objects.filter(user=request.user)
    return render(request,'profile.html',{'profile':profile,'booking':booking})

# deleting booking
@login_required
def delBooking(request,id):
    bookingid = BoatBooking.objects.get(id=id)
    bookingid.delete()
    return redirect('profile')

# Update Page

def updateProfile(request,id):
    profile = Profile.objects.get(id=id)
    if request.method == 'POST':
        form = Update(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = Update(instance=profile)
        return render(request,'update.html',{'form':form})
    
# Booking Page
@login_required(login_url='login')
def bookingForm(request):
    if request.method=='POST':
        form = BookingRegister(request.POST)
        subject = 'Thanks for booking from our website'
        message = "Dear {request.user},\n\nWe have received your booking and we are looking forward to serving you."
        from_email = settings.EMAIL_HOST_USER
        to_email = [form.data['email']]
        existing_booking = BoatBooking.objects.filter(
            user=request.user,
            check_in_date__gte=timezone.now() - timezone.timedelta(days=7) 
        ).exists()

        if existing_booking:
            messages.error(request, 'You already have an active booking.')
            return render(request,'messages.html')    
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assign the logged-in user to the booking
            booking.save()
            send_mail(subject,message,from_email,to_email)
            return render(request,'success.html')
        else:
            messages.error(request, 'There seems to be some trouble while trying to book your boat try again after some time')
    else:
        form = BookingRegister()
    return render(request,'booking.html',{'form':form})



# login 

def loginPage(request):
    if request.method=='POST':
        usern = request.POST['username']
        passw = request.POST['password']
        user = authenticate(request, username=usern, password=passw)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Incorrect credientials')
            return render(request,'messages.html')       
    return render(request,'login.html')

# log-out

def logOut(request):
    logout(request)
    return redirect(home)
    
