from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Booking

# Create your views here.
def home(request):
    if request.method=="POST":
      customerName = request.POST.get("cstname")
      customerEmail =  request.POST.get("cstemail")
      custOccupation =  request.POST.get("Occupation") 
      rNumber = request.POST.get("cstroom ")
      numberOfNight = request.POST.get("num_night")
      checkIn = request.POST.get("checkindate") 
      checkOut = request.POST.get("checkoutdate")
      bill = request.POST.get("cstamount")
      
      new_data = Booking(customerName=customerName, customerEmail = customerEmail,
                         custOccupation = custOccupation, rNumber =rNumber,
                         numberOfNight = numberOfNight, checkIn = checkIn, checkOut= checkOut,
                         bill = bill
                         )
      new_data.save()
      messages.success(request, "Occupant Added Successfully" )
      return redirect("home:feed")
    return render(request, "home/entry.html")

def feedback(request):
    return render(request, "home/feedBack.html")

# cstname       customerName
# cstemail      customerEmail 
# Occupation    custOccupation 
# cstroom       roomNumber    
# num_night     numberOfNight 
# checkindate   checkIn
# checkoutdate  checkOut     
# cstamount     bill 