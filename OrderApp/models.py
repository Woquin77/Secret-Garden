from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    flower_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.customer_name