from django.db import models

class Customer(models.Model):
    CustomerID = models.CharField(max_length=5, primary_key=True)
    CompanyName = models.CharField(max_length=100)
    ContactName = models.CharField(max_length=100)
    ContactTitle = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    Region = models.CharField(max_length=50, null=True, blank=True)
    PostalCode = models.CharField(max_length=20, null=True)
    Country = models.CharField(max_length=50)
    Phone = models.CharField(max_length=20, null=True)
    Fax = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.CompanyName
    
    class Meta:
        managed = True
        db_table = 'Customers'