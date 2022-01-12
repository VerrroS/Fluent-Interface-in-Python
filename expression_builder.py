
class Pizza:
    def __init__(self, name):
        self.restaurant = None
        self.name = name
        self.toppings = []
        self.price = None
        self.rating = None

    def at(self, restaurant):
        self.restaurant = restaurant
        return self

    def for_(self, price):
        if type(price) is float or type(price) is int:
            self.price = price
        else:
            raise TypeError("Price must be a number")
        return self

    def with_(self, toppings):
        for topping in toppings:
            self.toppings.append(topping)
        return self

    def rated(self, rating):
        if type(rating) is int:
            if rating in range(1, 6):
                self.rating = rating
            else:
                raise ValueError("Rating must be between 1 and 5")
        else:
            raise TypeError("Rating must be an integer")
        return self

    def __call__(self):
        if self.restaurant is None:
            raise ValueError("You must specify a restaurant")
        if self.price is None:
            raise ValueError("You must specify a price")
        else:
            if self.rating is None:
                self.rating = "no"
            if len(self.toppings) == 0:
                self.toppings = "no specific toppings"
            else:
                self.toppings = " and ".join(self.toppings)
            return print(f'{self.name} at {self.restaurant} with {self.toppings} is {self.price}'
                         f' dollars and has {self.rating} stars.')


new_pizza = Pizza("Pepperoni").rated(5).for_(10.99).at('Pizza Hut')()
