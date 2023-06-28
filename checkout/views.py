from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NO3ChF76CufBdvKkJTW1jz01g98EPHMQ0kAGAwc33wdUd00p6ENtleKvlJeMcAojKGLwew18TSnoFPt6czl6Ggn00T2kI76nF',
        'client_secret': 'sk_test_51NO3ChF76CufBdvKQHXuWL3mv85L4a4eh7MIM1ahVHQvS4t889mfmTHAozF1GIIeJ9NcodOdi6Z8lK1zUIyRskSH00SGItf5Mv',
    }

    return render(request, template, context)