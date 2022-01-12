
class Pizza:
    def __init__(self, name):
        self.restaurant = None
        self.name = name
        self.toppings = []
        self.price = None
        self.rating = None
        self.method = None

    def at(self, restaurant):
        self.restaurant = restaurant
        self.method = self.check()
        return self

    def for_(self, price):
        if type(price) is float or type(price) is int:
            self.price = price
        else:
            raise TypeError("Price must be a number")
        self.method = self.check()
        return self

    def with_(self, toppings):
        for topping in toppings:
            self.toppings.append(topping)
        self.method = self.check()
        return self

    def rated(self, rating):
        if type(rating) is int:
            if rating in range(1, 6):
                self.rating = rating
            else:
                raise ValueError("Rating must be between 1 and 5")
        else:
            raise TypeError("Rating must be an integer")
        self.method = self.check()
        return self

    def __call__(self):
        if self.method:
            return self.method()
        return None

    def check(self):
        if self.restaurant:
            if self.price:
                if self.toppings:
                    if self.rating:
                        return lambda: show_input(self.name, self.restaurant, self.price, self.toppings, self.rating)
        else:
            raise ValueError("Restaurant is required")


def show_input(name, restaurant, price, toppings, rating):
    print(f'{name} at {restaurant} with {" and ".join(toppings)} is {price} dollars and has {rating} stars.')


new_pizza = Pizza("Pepperoni").at('Pizza Hut').for_(10.99).with_(['Pepperoni', 'Fungi']).rated(5)()
