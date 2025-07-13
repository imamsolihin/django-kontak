from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def kontak_view(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        email = request.POST['email']
        pesan = request.POST['pesan']

        subject = f"Pesan dari {nama}"
        message = f"Email: {email}\n\nPesan:\n{pesan}"
        recipient = ['akunturkey111@gmail.com']  # Ganti dengan emailmu

        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient)
        return redirect('thanks')

    return render(request, 'form.html')
