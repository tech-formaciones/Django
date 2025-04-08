from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Customer
from .forms import CustomersForm

# Vista listado de clientes
def customers_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers_list.html', {'customers' : customers})

def customer_detail(request, customer_id):
    # customer = Customer.objects.get()
    customer = get_object_or_404(Customer, CustomerID = customer_id)

    form = CustomersForm(instance=customer)

    return render(request, 'customers_detail.html', {'customer' : customer, 'form': form})

def temp(request): pass