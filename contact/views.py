from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    """A view to return contact form and page"""
    form = ContactForm()

    """ Customer must be logged in to submit the contact form """
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your from has been sent. Thank you.')
            return redirect(reverse('home'))
        else:
            messages.error(request,
                           'Something went wrong. Please try again.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form
    }
    return render(request, template, context)
