from django.shortcuts import render

def doctorInterface(request):
    return render(request, 'doctor.html')

def appointInterface(request):
    doctorName = request.GET['doctorName']
    return render(request, 'appointment.html', {'doctorName': doctorName})

def displayAppoint(request):

    name = request.GET['name']
    age = request.GET['age']
    gender = request.GET['gender']
    blood = request.GET['blood']
    mobile = request.GET['mobile']
    email = request.GET['email']
    appoint_date = request.GET['appoint_date']
    address = request.GET['address']
    city = request.GET['city']
    return render(request, 'displayAppoint.html', {'name': name, 'age': age, 'gender': gender, 'blood': blood, 'mobile': mobile, 'appoint_date': appoint_date, 'address': address, 'city': city, 'email': email})