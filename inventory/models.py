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
    item_image = models.ImageField(null=True,blank=True,upload_to='images/')
    def __str__(self):
        return self.item_name
    
    @property
    def get_photo_url(self):
        if self.item_image and hasattr(self.item_image, 'url'):
            return self.item_image.url
        else:
            return "/static/images/user.jpg"
        
    def get_absolute_url(self):
        return reverse('menu-list')


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
