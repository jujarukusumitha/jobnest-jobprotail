from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hrdetails

    
def inserthrdetails(request):
    if request.method == 'POST':  # Make sure method is POST
        # Extract data from the form
        id = int(request.POST['t1'])
        companyname = request.POST['t2']
        vacancys = int(request.POST['t3'])
        role = request.POST['t4']
        package = int(request.POST['t5'])
        experience = int(request.POST['t6'])
        skills = request.POST['t7']
        location = request.POST['t8']
        startdate = request.POST['t9']
        deadline = request.POST['t10']
        phonenumber = request.POST['t11']

        # Create new Hrdetails object and save it to the database
        res  = Hrdetails(
            Id=id,
            Companyname=companyname,
            Vacancys=vacancys,
            Role=role,
            Package=package,
            Experience=experience,
            Skills=skills,
            Location=location,
            Startdate=startdate,
            Deadline=deadline,
            Phonenumber=phonenumber
        )
        res.save()  # Save the object to the database

        return HttpResponse('Data updated sucessfully')  # Redirect to a success page (update the URL)
    else:
        return render(request, 'hrpost.html')  # Render form template for GET request


# Create your views here.
def gethrdetails(request, no):
    # Fetch the specific record by its ID or return a 404 if not found

    if request.method == "POST":
        # Update the existing object with form data
        id=int(request.Post['t1'])
        companyname = request.POST['t2']
        vacancys = int(request.POST['t3'])
        role = request.POST['t4']
        package = int(request.POST['t5'])
        experience = int(request.POST['t6'])
        skills = request.POST['t7']
        location = request.POST['t8']
        startdate = request.POST['t9']
        deadline = request.POST['t10']
        phonenumber = request.POST['t11']
        res=Hrdetails(Id=id,Companyname=companyname,Vacancys=vacancys,Role=role,Package=package,Experience=experience,Skills=skills,Location=location,Startdate=startdate,Deadline=deadline,Phonenumber=phonenumber)

        res.save()  # Save the updated record

        return HttpResponse('Your data was updated successfully')
    res=Hrdetails.objects.filter(Id=no)

    # Render the update form, passing the current data
    return render(request, 'update.html', {'data': res})
def deletehrdetails(request,no):
    res = Hrdetails.objects.filter(Id=no)
    res.delete()
    return redirect('selecturl')
    
