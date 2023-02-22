from django.shortcuts import render,redirect
from .models import QrCode

def index(request):

    if request.method == "POST":
        name = request.POST['name']
        QrCode.objects.create(name=name)
        return redirect('/')

    qr_codes = QrCode.objects.all()

    return render(request, 'index.html',{'qr_codes': qr_codes})