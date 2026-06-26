from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def index(request):
    return render(request,'home.html')

def bookings(request):
    return render(request,'booking.html')

def booking2(request):
    return render(request,'booking2.html')





from django.core.mail import send_mail
from django.conf import settings

def booking(request):
    message = ""

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        service = request.POST.get("service")
        date = request.POST.get("date")
        guests = request.POST.get("guests")

        subject = f"New Booking - {service}"

        body = f"""
New Booking Received

Name: {name}
Email: {email}
Phone: {phone}

Service: {service}
Date: {date}
Guests: {guests}
"""

        try:
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                ["freshmartshop123@gmail.com"],   # Replace with your email
                fail_silently=False,
            )
            message = "Booking Sent Successfully!"
        except Exception as e:
            message = str(e)
            print(e)

    return render(request, "booking_email.html", {"message": message})