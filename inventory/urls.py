from django.urls import path
from .views import *



urlpatterns = [
    path('home/',HomePage.as_view(),name='home'),
    path('ingredients/', InventoryListView.as_view(), name='ingredient-list'),
    path('ingredient/<int:pk>/delete/', InventoryDeleteView.as_view(), name='ingredient-delete'),
    path('menu/', MenuDetailsView.as_view(), name='menu-list'),
    path('purchases/', PurchasesListView.as_view(), name='purchase-list'),
    path('profit/', ProfitView.as_view(), name='profit'),

    path('ingredients/add_ingredient/', AddIngredientFormView.as_view(),name='add-ingredient'),
    path('ingredients/add_menuitem/',AddMenuItem.as_view(),name='add-menuitem'),
    path('ingredients/add_recipe_requirement/',RecipeRequirementFormView.as_view(),name='add-recipe'),
    path('menu/purchases/',AddPurchasesFormView.as_view(),name='add-purchases')
]
