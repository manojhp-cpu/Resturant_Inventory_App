from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ingredient_name
    
    def get_absolute_url(self):
        return reverse('ingredient-list')


class MenuItem(models.Model):
    item_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, default='g')

    def __str__(self):
        return f"{self.menu_item}"
    
    


class CustomerPurchases(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self):
        if not self.price:
            self.price = self.menu_item.price
        super().save()
