ice_cream_sundae = {
   "scoops": 2,
   "Flavor1": "Strawberry swirl",
   "Flavor2": "Almond crunch",
   "Topping": "Roasted nuts",
   "Syrup": "Strawberry sauce"
}

ice_cream_sundae.update({"Syrup": "Caramel sauce"})      # We change the value of a pre-defined key in a dictionary
ice_cream_sundae.update({"Price": "150 rupees"})      # We can also add a new key: value pair
print(ice_cream_sundae)

ice_cream_sundae.pop("Flavor2")     # we can remove a specified item from the dictionary using this method
print(ice_cream_sundae)

ice_cream_sundae.clear()      # empties the dictionary
print(ice_cream_sundae)
