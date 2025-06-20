class Restaurant:
    
    
    def __init__(self,name,cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served =0
    
    
    def describe_restaurant(self):
        """print the restaurant description;"""
        print(f"The Restaurant name is {self.name} and serves {self.cuisine_type}.")
        
    def open_restaurant(self):
        """Display the restaurant is open."""
        print(f"{self.name} is open now !")
        
    def set_number_served(self,number):
        """Set the number of customers served."""
        self.number_served = number
        
        
    def increment_number_seerved(self,number):
        """Increment the number of customer served."""
        self.number_served += number
        
restaurant = Restaurant("Sushi",'Japanese')
    
print(f"Restaurant name is {restaurant.name}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"Number of customers served: {restaurant.number_served}.")
restaurant.number_served = 20
print(f"Number of customers served: {restaurant.number_served}.")
restaurant.set_number_served(50)
print(f"Number of customers served: {restaurant.number_served}.")
restaurant.increment_number_seerved(10)
print(f"Number of customers served: {restaurant.number_served}.")

# instance 2
restaurant2 = Restaurant("Taco Bell",'Mexican')

print(f"Restaurant name is {restaurant2.name}.")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()


# instance 3
restaurant3 = Restaurant("Pasta House",'Italian')
print(f"Restaurant name is {restaurant3.name}.")
restaurant3.describe_restaurant()
restaurant3.open_restaurant()





class User:
    '''A simple attempt to model a user profile.'''
    
    
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts =0
    
    
    def describe_user(self):
        """Display user information"""
        print(f"User's name is {self.first_name} {self.last_name}.")
        
    def greet_user(self):
        """Display a greeting to the user."""
        print(f"Hello {self.first_name} {self.last_name}, welcome back !")
    
    def increment_login_attempts(self):
        """Increment the number of login attempts by 1."""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """Resets the login attempts to 0."""
        self.login_attempts =0
        
    
user = User("John","Doe")
user.describe_user()
user.greet_user()

user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}.")
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}.")
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}.")