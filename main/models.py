from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self) -> str:
        return f"{self.first_name} - {self.city} = {self.state}"