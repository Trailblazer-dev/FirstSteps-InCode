from django.shortcuts import render

# Create your views here.
# Define a view for the index page of pizzas
def index(request):
    """The home page for pizzas."""
    return render(request, 'pizzas/index.html')
