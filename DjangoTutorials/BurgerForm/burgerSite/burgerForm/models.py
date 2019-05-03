from django.conf import settings
from django.db import models
from django.utils import timezone

class Order(models.Model):
    order_number = models.AutoField(primary_key = True)
    customer_name = models.CharField(max_length = 200)
    protein = models.CharField(max_length = 200)
    num_patties = models.IntegerField(default = 1)
    COOK_OPTIONS = (
        (1, 'Rare'),
        (2, 'Medium Rare'),
        (3, 'Medium'),
        (4, 'Medium Well'),
        (5, 'Well Done'),
    )
    cook = models.IntegerField(default = 3, choices = COOK_OPTIONS)
    lettice = models.BooleanField(default = False)
    tomato = models.BooleanField(default = False)
    onion = models.BooleanField(default = False)
    cheese = models.BooleanField(default = False)
    BUN_TYPES = (
        ('Sesame', 'Sesame'),
        ('Potato', 'Potato'),
        ('Pretzel', 'Pretzel'),
    )
    bun = models.CharField(max_length = 7, default = 'Sesame', choices = BUN_TYPES)
    SAUCE_TYPES = (
        ('Ketchup', 'Ketchup'),
        ('Mustard', 'Mustard'),
        ('BBQ', 'BBQ'),
        ('Mayo', 'Mayo'),
    )
    sauce = models.CharField(max_length = 7, default = "Ketchup", choices = SAUCE_TYPES)
    comments = models.CharField(max_length = 200, blank = True)
    date = models.DateTimeField(default = timezone.now)\

    def place_order(self):
        self.save()

    def __str__(self):
        return str(self.order_number)
