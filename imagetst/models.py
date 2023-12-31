from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Heading(models.Model):
    header_name = models.CharField(max_length=150,null= True)

    def __str__(self):
        return self.header_name

class Slide(models.Model):
    header = models.ForeignKey(Heading, on_delete=models.CASCADE, null=True)
    images = models.ImageField(upload_to='slide_img', null= True)
    description = models.TextField(null= True,blank=True)
    location = models.CharField(max_length=150,null= True)

    def __str__(self):
        return self.location
   

class Menu(models.Model):
    menu_time = models.CharField(max_length=150,null=True)
    menu = models.TextField(null=True)

    def __str__(self):
        return self.menu_time

class HouseBoat(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='slide_img', null= True)
    price = models.IntegerField(blank=True)
    description = models.TextField(null= True,blank=True)
    main_des = models.TextField(null= True,blank=True)
    about_destination = models.TextField(null= True,blank=True)
    quick_facts = models.TextField(null= True,blank=True)
    
    def __str__(self):
        return self.title

class Package(models.Model):
    image = models.ImageField(upload_to='slide_img', null=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null= True,blank=True)
    main_des = models.TextField(null= True,blank=True)
    about_destination = models.TextField(null= True,blank=True)
    quick_facts = models.TextField(null= True,blank=True)

    def __str__(self):
        return self.title

class BoatBooking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    houseboat = models.ForeignKey(HouseBoat, on_delete=models.CASCADE,null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE,null=True)
    check_in_date = models.DateField(null=True)
    check_out_date = models.DateField(null=True)
    rooms = models.PositiveSmallIntegerField(null=True,default=1)
    email = models.EmailField(null=True)



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    bio = models.TextField(null=True)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    profile_image = models.ImageField(null=True,upload_to='slide_img')

    def __str__(self):
        return self.user.username
