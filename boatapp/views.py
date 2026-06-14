from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'home.html')

def bookings(request):
    return render(request,'booking.html')

def booking2(request):
    return render(request,'booking2.html')