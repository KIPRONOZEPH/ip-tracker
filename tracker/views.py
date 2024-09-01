from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required  
from django.conf import settings
import requests

@login_required
def index(request):
    return render(request, 'tracker/index.html')

@login_required
def services(request):
    return render(request, 'tracker/services.html')

@login_required
def about(request):
    return render(request, 'tracker/about.html')

@login_required
def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Sending the email
        send_mail(
            subject=f"Contact Form Submission: {subject}",
            message=message,
            from_email=settings.EMAIL_HOST_USER, 
            recipient_list=[settings.EMAIL_HOST_USER],  
            fail_silently=False,
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('/')  

    return render(request, 'tracker/contact.html')

@login_required
def track_ip(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        
        location_data = {
            "Ip Address": ip_address,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name"),
            "Ip Address Type": response.get("version"),
            "Region Code": response.get("region_code"),
            # "Postal Code": response.get("postal"),
            "Latitude": response.get("latitude"),
            "Longitude": response.get("longitude"),
            "TimeZone": response.get("timezone"),
            "Country code": response.get("country_calling_code"),
            # "Currency": response.get("currency"),
            # "Currency Name": response.get("currency_name"),
            # "Languages": response.get("languages"),
            "Country Area": response.get("country_area"),
            # "Population": response.get("country_population"),
            "ASN": response.get("asn"),
            # "Organization": response.get("org")
        }
        
        map_url = f"https://google.com/maps/place/{response.get('latitude')},{response.get('longitude')}/@{response.get('latitude')},{response.get('longitude')},16z"
        
        return render(request, 'tracker/track.html', {'location_data': location_data, 'map_url': map_url})
    
    return render(request, 'tracker/track.html')
