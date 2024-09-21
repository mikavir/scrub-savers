from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.
def contact(request):
    """ Renders the contact page and allow users to send message """
    """ A view to return the contact page """
    form = ContactForm()

    if request.method == 'POST':
        sender = settings.DEFAULT_FROM_EMAIL
        cust_email = request.POST.get('email')
        name = request.POST.get('name')
        subject = "Thank you for reaching out!"
        body = render_to_string(
            'contact/auto_reply/email_body.txt',
            {'name': name})
        
        send_mail(
            subject,
            body,
            sender,
            [cust_email]
        )   
    
    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)