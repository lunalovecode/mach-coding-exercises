flavors = ["vanilla", "chocolate", "strawberry", "cookies n' cream", "bubblegum"]
toppings = ["almonds", "banana slices", "chocolate syrup", "caramel syrup", "white chocolate chips"]
ice_cream = dict(zip(flavors, toppings))

ice_cream["chocolate"] = "blueberries"

ice_cream.update({"matcha": "pistachios", "ube": "mango slices"})

print(ice_cream)