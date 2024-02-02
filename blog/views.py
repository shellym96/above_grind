from django.shortcuts import render, redirect


def blog(request):

    template = "blog/blog.html"
    return render(request, template)