from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
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

def customer_create(request):
    if(request.method == 'POST'):
        Customer.objects.create(
            CustomerID = request.POST['CustomerID'],
            CompanyName = request.POST['CompanyName'],
            ContactName = request.POST['ContactName'],
            ContactTitle = request.POST['ContactTitle'],
            Address = request.POST['Address'],
        )

        return HttpResponseRedirect('/customer')                  # Opción 1: Especificamos la URL completa
        return HttpResponseRedirect(reverse('customers_list'))    # Opción 2: Especificamos el name de la ruta
    else:
        form = CustomersForm()
        return render(request, 'customers_create.html', { 'form' : form})

def temp(request): pass