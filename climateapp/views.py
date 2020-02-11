from django.shortcuts import render
from .models import Politician
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

def thanks(request):
    return render(request, 'thanks.html')


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipients = ['jarnagin.z@northeastern.edu']
            # redirect to a new URL:
            try:
                send_mail(subject, message + "\n\nSender:\t" + sender, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    politicians = Politician.objects.all()
    distinct_state = Politician.objects.order_by('state').values('state').distinct()[1:]
    return render(request, 'index.html', ({'politicians': politicians, 'distinct_state': distinct_state, 'form': form}))
