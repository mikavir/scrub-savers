from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from .forms import ContactForm
from .models import Contact


def contact(request):
    """ Renders the contact page and allow users to send message
    https://mailtrap.io/blog/django-contact-form/ """
    """ A view to return the contact page """
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sender = settings.DEFAULT_FROM_EMAIL
            cust_email = request.POST.get('email')
            name = request.POST.get('name')
            subject = " We’ve Got Your Message! 🩺✨"
            body = render_to_string(
                'contact/auto_reply/email_body.txt',
                {'name': name})
            try:
                send_mail(
                    subject,
                    body,
                    sender,
                    [cust_email]
                )
                return redirect("success")
            except Exception as e:
                # Log the error for debugging purposes
                messages.error(
                    request,
                    (f"Failed to send email to {cust_email}. Error: {str(e)}")
                )
        else:
            messages.error(
                request,
                ("Something went wrong, Please try again")
            )

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def success(request):
    """ Renders when user have successfuly sent an email"""
    return render(request, 'contact/success.html')
