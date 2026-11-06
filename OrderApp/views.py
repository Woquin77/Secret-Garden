from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order


@login_required(login_url='login')
def order_list(request):
    orders = Order.objects.all()

    return render(request, 'orders.html', {
        'orders': orders
    })


@login_required(login_url='login')
def add_order(request):
    if request.method == "POST":
        Order.objects.create(
            customer_name=request.POST.get('customer_name'),
            flower_name=request.POST.get('flower_name'),
            quantity=request.POST.get('quantity'),
            total_price=request.POST.get('total_price'),
        )

        messages.success(request, 'Order added successfully!')
        return redirect('orders')

    return render(request, 'add_order.html')

@login_required(login_url='login')
def edit_order(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == "POST":
        order.customer_name = request.POST.get('customer_name')
        order.flower_name = request.POST.get('flower_name')
        order.quantity = request.POST.get('quantity')
        order.total_price = request.POST.get('total_price')

        order.save()

        messages.success(request, 'Order updated successfully!')
        return redirect('orders')

    return render(request, 'edit_order.html', {
        'order': order
    })

@login_required(login_url='login')
def delete_order(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == "POST":
        order.delete()
        messages.success(request, 'Order deleted successfully!')

    return redirect('orders')
    