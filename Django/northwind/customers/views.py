from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views.generic import View, ListView, UpdateView, DeleteView, CreateView

from .models import Customers
from .forms import CustomersForm

import pymssql, requests

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
    
# Vista para mostrar y actulizar un Cliente, opción 1
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

# Vista para mostrar y actulizar un Cliente, opción 2
class CustomerDetailView2(UpdateView):
    model = Customers
    form_class = CustomersForm
    template_name = 'customer_details.html'
    context_object_name = 'customers'

    def get_object(self, queryset = None):
        customer_id = self.kwargs.get('customer_id')
        return get_object_or_404(Customers.objects.using('northwind'), customerid = customer_id)
    
    def form_valid(self, form):
        form.save()
        return redirect(reverse('customer_list'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = 'details'

        return context

# Vista para crear un Cliente, opción 1
class CustomerCreateView(View):
    model = Customers
    template_name = 'customer_details.html'

    def get(self, request):
        form = CustomersForm()

        context =  {
            'form': form,
            'view_name': 'create'
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomersForm(request.POST)

        if(form.is_valid()):
            new_customer = form.save(commit=False)
            new_customer.save(using='northwind')

            return redirect(reverse('customer_list'))
        else:
            context =  {
                'form': form,
                'view_name': 'create'
            }

            return render(request, self.template_name, context)
        
# Vista para crear un Cliente, opción 2
class CustomerCreateView2(CreateView):
    model = Customers
    form_class = CustomersForm
    template_name = 'customer_details.html'

    def form_valid(self, form):
        new_customer = form.save(commit=False)
        new_customer.save(using='northwind')

        return redirect(reverse('customer_list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = 'create'

        return context
    
# Vista para eleminar un cliente, opción 1
class CustomerDeleteView(View):
    context_object_name = 'customer'
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer_list')

    def get(self, request, customer_id):
        customer = get_object_or_404(Customers.objects.using('northwind'), customerid = customer_id)
        return render(request, self.template_name, { self.context_object_name: customer})

    def post(self, request, customer_id):
        customer = get_object_or_404(Customers.objects.using('northwind'), customerid = customer_id)
        customer.delete()

        return redirect(self.success_url)

# Vista para eleminar un cliente, opción 2
class CutomerDeleteView2(DeleteView):
    model = Customers
    context_object_name = 'customer'
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer_list')

    def get_object(self, queryset = None):
        customer_id = self.kwargs.get('customer_id')
        return Customers.objects.using('northwind').get(customerid=customer_id)
        return get_object_or_404(Customers.objects.using('northwind'), customerid = customer_id)
    
########################################################################################


# Vista para un listado de Clientes, cliente nativo
class CustomerListViewNativeClient(View):
    template_name = 'customer_list2.html'
    context_object_name = 'customers'

    connection = pymssql.connect(
        server="localhost",
        port="1433",
        user="dbuser",
        password="demo",
        database="Northwind"
    )

    def get(self, request):
        cursor = self.connection.cursor()
        cursor = self.connection.cursor(as_dict=True)

        cursor.execute("SELECT * FROM dbo.Customers")
        customers = cursor.fetchall()

        return render(request, self.template_name, {self.context_object_name: customers})

# Vista para un listado de Clientes, cliente HTTP
class CustomerListViewHTTPClient(View):
    template_name = 'customer_list.html'
    context_object_name = 'customers'
    api_url = 'http://127.0.0.1:5000/customers'
    customers = []

    def get(self, request):
        try:
            response = requests.get(self.api_url, headers={'X-API-KEY': '123456secret'})
            response.raise_for_status()
            customers = response.json()
        except:
            self.customers = []
        finally:
            return render(request, self.template_name, {self.context_object_name: customers})