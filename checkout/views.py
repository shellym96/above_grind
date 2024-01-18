from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There is nothing in your cart at the moment!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_puvlic_key': 'pk_test_51OM9dxBcXVF7OF7TsVqUpwXWOaqCXnHetj7Hw2yhzevrnJSGHAJPHaRwTiOQu4KFbjk4I6f171auAY005py3Qo2500ePCgpxYd',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)