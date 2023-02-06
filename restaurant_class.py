from datetime import datetime


class Restaurant:
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.restaurant_cuisine_type = cuisine

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}")
        print(f"Cuisine type is {self.restaurant_cuisine_type}")

    def open_restaurant(self):
        time = datetime.now()
        hour = int(time.strftime("%H"))
        if 9 < hour < 23:
            print(f"{self.restaurant_name} is Open")
        else:
            print(f"{self.restaurant_name} is Closed")


r1 = Restaurant("Behrouz", "South Indian")
print(r1.restaurant_name)
print(r1.restaurant_cuisine_type)
r2 = Restaurant("Tatva", "North Indian")
print(r2.restaurant_name)
print(r2.restaurant_cuisine_type)
r3 = Restaurant("AB's", "Barbeque")
print(r3.restaurant_name)
print(r3.restaurant_cuisine_type)
r1.describe_restaurant()
r1.open_restaurant()
r2.describe_restaurant()
r2.open_restaurant()
r3.describe_restaurant()
r3.open_restaurant()
