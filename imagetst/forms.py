from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import BoatBooking,HouseBoat,Package,PackageReview

class Regform(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs = {
            'placeholder':'Enter Your Name',
            'class':'form-control'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'placeholder':'Enter Your Name',
            'class':'form-control'
        }
    ))
    password1 = forms.CharField(widget= forms.PasswordInput(
        attrs = {
            'placeholder':'Enter Password',
            'class':'form-control'
        }
    ))
    password2 = forms.CharField(widget= forms.PasswordInput(
        attrs = {
            'placeholder':'Enter Password',
            'class':'form-control'
        }
    ))
    class Meta:
        model = User
        fields = ['username','email']

class Update(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs = {
            'placeholder':'Enter Your Name',
            'class':'form-control'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs ={
            'placeholder':'Enter Your Name',
            'class':'form-control'            
        }
    ))
    bio = forms.CharField(widget=forms.TextInput(
        attrs ={
            'placeholder':'Enter Your Bio',
            'class':'form-control'            
        }
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs ={
            'placeholder':'Enter Your Phone',
            'class':'form-control'            
        }
    ))
    profile_image = forms.ImageField(widget=forms.FileInput(
        attrs ={
            'placeholder':'Enter Your Bio',
            'class':'form-control'            
        }
    ))
    
    class Meta:
        model = User
        fields = ['name','email','bio','phone','profile_image']

class BookingRegister(forms.ModelForm):

    houseboat = forms.ModelChoiceField(queryset=HouseBoat.objects.all(), widget=forms.Select(
        attrs={
            'class' : 'form-control'
        }
    ))
# HOUSEBOATS = (
#     ("Three Bedroom Premium","Three Bedroom Premium"),
#     ("Two Bedroom Premium","Two Bedroom Premium"),
#     ("One Bedroom Premium","One Bedroom Premium"),
#     ("Three Bedroom Deluxe","Three Bedroom Deluxe"),
#     ("Two Bedroom Deluxe","Two Bedroom Deluxe"),
#     ("One Bedroom Deluxe","One Bedroom Deluxe"),
# )
#     houseboat = forms.ChoiceField(
#         choices=HOUSEBOATS,
#         widget=forms.Select(
#             attrs={
#                 'placeholder':'Select a houseboat...',
#                 'class' : 'form-control'
#             }
#         )
#     )
    package = forms.ModelChoiceField(queryset=Package.objects.all(),widget=forms.Select(
        attrs={
            'class' : 'form-control'
        }
    ))
    check_in_date = forms.DateField(widget=forms.DateInput(
        attrs={
            'type' : 'date',
            'placeholder' : 'yyyy-mm-dd',
            'class' : 'form-control'
        }
    ))
    check_out_date = forms.DateField(widget=forms.DateInput(
        attrs={
            'type' : 'date',
            'placeholder' : 'yyyy-mm-dd',
            'class' : 'form-control'
        }
    ))
    rooms = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'placeholder': 'Enter the number of rooms needed',
            'class' : 'form-control'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Enter your email',
            'class' : 'form-control'
        }
    ))
    class Meta:
        model = BoatBooking
        fields = ['houseboat','package','check_in_date','check_out_date','rooms','email']

class ReviewForm(forms.ModelForm):
    RATING = (
    (1,"★☆☆☆☆"),
    (2,"★★☆☆☆"),
    (3,"★★★☆☆"),
    (4,"★★★★☆"),
    (5,"★★★★★")
)
    review = forms.CharField(
        widget=forms.TextInput(
        attrs={
            'placeholder':'Write a review...',
            'class': 'rev-inp'
        }
    ))
    rating = forms.ChoiceField(
        choices=RATING,
        widget=forms.Select(
        attrs={
            'class': 'rating'
        }
    ))
    class Meta:
        model = PackageReview
        fields = ['review', 'rating']