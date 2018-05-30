from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .forms import ContactForm


def index(request):
    form_class = ContactForm
    message = ""

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            contact_title = request.POST.get('contact_title', '')
            form_content = request.POST.get('contact_msg', '')

            email = EmailMessage(subject=contact_title, body=form_content, from_email=contact_email,
                                 to=('nowosad.smolec@gmail.com',))
            email.send()
            message = "Wiadomość wysłano."
            context = {'contact_form': ContactForm,
                       'message': message}
            return render(request, 'contact/index.html', context)
        else:
            message = "Nie udało się wysłać wiadomości."
            context = {'contact_form': form_class,
                       'message': message}
            return render(request, 'contact/index.html', context)
    else:
        context = {'contact_form': form_class,
                   'message': message}
        return render(request, 'contact/index.html', context)