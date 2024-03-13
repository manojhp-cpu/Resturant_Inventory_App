from django.contrib import admin
from .models import Ingredient,MenuItem,RecipeRequirement,CustomerPurchases

# Register your models here.
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass

@admin.register(RecipeRequirement)
class RecipeRequirementAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomerPurchases)
class CustomerPurchasesAdmin(admin.ModelAdmin):
    pass
