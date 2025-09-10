from django.shortcuts import render
from .models import Pizza

# Create your views here.
# Define a view for the index page of pizzas
def index(request):
    """The home page for pizzas."""
    return render(request, 'pizzas/index.html')

def menu(request):
    """The menu page for pizzas."""
    menu = Pizza.objects.values()
    context = {'menu': menu}
    return render(request, 'pizzas/menu.html', context)

def toppings(request, pizza_id):
    """Show details of a specific pizza and its toppings."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/topping.html', context)