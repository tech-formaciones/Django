from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views.generic import View, ListView, UpdateView, DeleteView, CreateView

from .models import Customers
from .forms import CustomersForm

def temp(request): pass

# Vista para un listado de Clientes, opción 1
class CustomerListView(View):
    model = Customers
    template_name = 'customer_list.html'
    context_object_name = 'customers'

    def get(self, request):
        customers = Customers.objects.using('northwind').all()

        return render(request, self.template_name, {self.context_object_name: customers})

# Vista para un listado de Clientes, opción 2    
class CustomerListView2(ListView):
    model = Customers
    template_name = 'customer_list.html'
    context_object_name = 'customers'
    queryset = Customers.objects.using('northwind').all()

# Vista para un listado de Clientes, opción 3
class CustomerListView2(ListView):    
    model = Customers
    template_name = 'customer_list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        return Customers.objects.using('northwind').all()
    
class CustomerDetailView(View):
    model = Customers
    template_name = 'customer_details.html'
    context_object_name = 'customers'

    def get(self, request, customer_id):
        customer = get_object_or_404(Customers.objects.using('northwind'), customerid = customer_id)
        form = CustomersForm(instance=customer)

        context = {
            self.context_object_name: customer,
            'form': form,
            'view_name': 'details'
        }

        return render(request, self.template_name, context)

    def post(self, request, customer_id):
        customer = get_object_or_404(Customers.objects.using('northwind'), customerid = customer_id)
        form = CustomersForm(request.POST, instance=customer)

        if(form.is_valid()):
            form.save()

            return redirect(reverse('customer_list'))
        else:
            return render(request, self.template_name, {'form': form, 'view_name': 'details'}) 