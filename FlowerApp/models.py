from django.db import models


class Flower(models.Model):
    CATEGORY_CHOICES = [
        ('Rose', 'Rose'),
        ('Tulip', 'Tulip'),
        ('Lily', 'Lily'),
        ('Orchid', 'Orchid'),
        ('Sunflower', 'Sunflower'),
    ]

    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True)

    def __str__(self):
        return self.name