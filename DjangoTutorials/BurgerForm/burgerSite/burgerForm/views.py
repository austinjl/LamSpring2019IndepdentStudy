from django.shortcuts import render
from django.utils import timezone
from .models import Order
from .forms import OrderForm
from django.shortcuts import redirect

def tickets(request):
    form = Order.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'burgerForm/tickets.html', {'form': form})

def order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect("/burger/tickets")
    else:
        form = OrderForm()
        return render(request, 'burgerForm/order_burger.html', {'form': form})
