from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Item
from .forms import OrderForm, ItemForm
from rest_framework import viewsets
from .serializers import ItemSerializer, OrderSerializer
from django.utils.timezone import now, localtime, make_aware
from datetime import timedelta
def home(request):
    items = Item.objects.all()
    return render(request, 'orders/home.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'orders/add_item.html', {'form': form})

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=item)
    return render(request, 'orders/edit_item.html', {'form': form, 'item': item})
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})



def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()

    items = Item.objects.all()

    return render(request, 'orders/add_order.html', {'form': form, 'items': items})


def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('order_list')

def search_orders(request):
    query = request.GET.get('query')
    status_filter = request.GET.get('status')

    if query:
        orders = Order.objects.filter(table_number__icontains=query) | Order.objects.filter(status__icontains=query)
    else:
        orders = Order.objects.all()

    if status_filter:
        orders = orders.filter(status=status_filter)

    return render(request, 'orders/order_list.html', {'orders': orders})


def update_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        return redirect('order_list')
    return render(request, 'orders/update_status.html', {'order': order})

def revenue_report(request):
    paid_orders = Order.objects.filter(status='paid')
    total_revenue = sum(order.total_price for order in paid_orders)

    # Calculate revenue for the current shift (e.g., last 8 hours)
    current_time = localtime(now())  # Get local time
    shift_start = current_time - timedelta(hours=8)  # Define a shift (last 8 hours)
    shift_orders = paid_orders.filter(created_at__gte=shift_start)
    shift_revenue = sum(order.total_price for order in shift_orders)
    return render(request, 'orders/revenue_report.html', {
        'total_revenue': total_revenue,
        'shift_revenue': shift_revenue
    })




class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer