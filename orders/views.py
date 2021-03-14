from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.conf import settings
#import stripe
#stripe.api_key = settings.STRIPE_SECRET_KEY 

def order_create( request ):
    cart = Cart(request)
    if request.method == 'POST':
        #charge = stripe.Charge.create(
            #amount='{:.0f}'.format(cart.get_total_price()*100),
            #currency='usd',
            #description='Pay By Credit Cart',
            #source=request.POST['stripeToken']
        #)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()




            # redirect  payment
            #request.session.modified = True

            #order.paid = True
            # store the unique transaction id
            #order.save()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
    	form = OrderCreateForm()
    	return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})