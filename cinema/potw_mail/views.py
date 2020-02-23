from django.shortcuts import render
from cinema.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail


def confirm(request):
    conf = forms.ConfirmMail()
    if request.method == 'POST':
        sub = forms.ConfirmMail(request.POST)
        subject = 'Potwierdzenie rezerwacji biletow'
        message = 'Zarezerwowales bilety w kiniem ... proszę zglosic sie najpozniej 15 minut przed seansem'
        recepient = str(sub['Email'].value())
        send_mail(subject,
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'send.html', {'recepient': recepient})
    return render(request, 'mail.html', {'form':conf})