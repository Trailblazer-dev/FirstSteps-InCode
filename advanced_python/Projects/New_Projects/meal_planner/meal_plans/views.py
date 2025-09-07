from django.shortcuts import render

# Create your views here.
# Define a view for the index page of meal plans
def index(request):
    """The home page for meal plans."""
    return render(request, 'meal_plans/index.html')
