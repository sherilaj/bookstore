from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Book, CartItem
from django.contrib import messages

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    action = request.POST.get('action')
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)

    
    if action == 'add':
        cart_item.quantity += 1
        cart_item.save()
        book.Stock -= 1
        book.save()
        messages.success(request, 'Item added to cart successfully.')
    elif action == 'remove':
        if cart_item.quantity > 0:
            cart_item.quantity -= 1
            cart_item.save()
            book.Stock += 1
            book.save()
            messages.success(request, 'Item removed from cart successfully.')
        if cart_item.quantity <= 0:
            cart_item.delete()
            messages.success(request, 'Item removed from cart successfully.')
        

    return redirect('cartapp:cartview')
   

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = 0
    for item in cart_items:
        item.total_price = item.book.OfferPrice * item.quantity
        total_price += item.total_price
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})