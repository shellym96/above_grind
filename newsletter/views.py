from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm


def newsletter(request):
    """
    View to display the newsletter signup form.
    """
    form = NewsletterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Thank for signing up to our newsletter")
            return redirect("home")
        # error
        messages.error(request, "Error: Please try again")
    template = "newsletter/newsletter.html"
    context = {
        "form": form,
    }
    return render(request, template, context)
