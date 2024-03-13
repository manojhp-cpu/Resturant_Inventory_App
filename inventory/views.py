from django.db.models import F, ExpressionWrapper, DecimalField
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import DeleteView, CreateView

from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchasesForm
from .models import Ingredient, CustomerPurchases, MenuItem, RecipeRequirement


# Create your views here.
class HomePage(TemplateView):
    template_name = 'inventory/home.html'


class InventoryListView(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
    context_object_name = 'ingredients'


class AddIngredientFormView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/add_ingredient.html'


class InventoryDeleteView(DeleteView):
    model = Ingredient
    success_url = reverse_lazy('ingredient-list')


class PurchasesListView(ListView):
    model = CustomerPurchases
    template_name = 'inventory/purchases.html'
    context_object_name = 'purchases'


class AddPurchasesFormView(CreateView):
    model = CustomerPurchases
    form_class = PurchasesForm
    template_name = 'inventory/add_purchases.html'


class MenuDetailsView(ListView):
    model = MenuItem
    template_name = 'menuitem_list.html'
    context_object_name = 'menuitems'


class AddMenuItem(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/add_menuitem.html'


class ProfitView(TemplateView):
    template_name = 'inventory/profitandrevenue.html'  # Template to render the profit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calculate total revenue
        total_revenue = CustomerPurchases.objects.aggregate(total_revenue=Sum('price'))['total_revenue']

        # Calculate total cost
        total_cost = RecipeRequirement.objects.annotate(
            total_cost=ExpressionWrapper(F('quantity') * F('ingredient__unit_price'), output_field=DecimalField())
        ).aggregate(total_cost=Sum('total_cost'))['total_cost']

        # Calculate profit
        profit = total_revenue - total_cost if total_cost else 0

        context['profit'] = profit
        return context


class RecipeRequirementFormView(CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = 'inventory/add_reciperequirement.html'
