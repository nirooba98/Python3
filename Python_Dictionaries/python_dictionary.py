"""
A dictionary collection of data in which the data value are stores as Key: Value pairs.
A dictionary can contain many number of data values each of which is separated by a comma.
There are no duplicate values allowed in a dictionary. i.e. Each key is different and unique.
"""

ice_cream_sundae = {
   "scoops": 2,      # These are (Key: value) pairs. "scoops" is key and 2 is its value.
   "Flavor1": "Strawberry swirl",
   "Flavor2": "Almond crunch",
   "Topping": "Roasted nuts",
   "Syrup": "Strawberry sauce",    # dictionaries Cannot contain duplicate values. This value for the key, "Syrup"
   "Syrup": "Chocolate sauce"      # will be replaced by the new value in the next line
}


print(ice_cream_sundae)
print(ice_cream_sundae["scoops"])
print(ice_cream_sundae.get("Flavor2"))
print(ice_cream_sundae.get("vanilla"))    # does not print values which are not defined. Returns 'None'.
