from django import forms
from . models import Ingredient,MenuItem,RecipeRequirement,CustomerPurchases

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('ingredient_name','quantity','unit','unit_price')

        widgets = {
            'ingredient_name':forms.TextInput(attrs={'class':'form-control'}),
            'quantity': forms.TextInput(attrs={'class':'form-control'}),
            'unit': forms.TextInput(attrs={'class':'form-control'}),
            'unit_price': forms.TextInput(attrs={'class':'form-control'}),
        }

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

        widgets = {
            'item_name':forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
        }

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"

        widgets = {
            'menu_item':forms.TextInput(attrs={'class':'form-control'}),
            'ingredient': forms.TextInput(attrs={'class':'form-control'}),
            'quantity': forms.TextInput(attrs={'class':'form-control'}),
            'unit': forms.TextInput(attrs={'class':'form-control'}),
        }

class PurchasesForm(forms.ModelForm):
    class Meta:
        model = CustomerPurchases
        fields = "__all__"

        widgets = {
            'menu_item':forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
        }




