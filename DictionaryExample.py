# Dictionary Example

nation = {"Nepal" : "Kathmandu",
          "India" : "New Delhi",
          "China" : "Beijing",
          "USA"   : "Washington DC",
          "UK"    : "London"}

print("Nation Dictionary")
print(nation)

print("Capital of Nepal is " + nation["Nepal"])
print("Capital of USA is " + nation.get("USA"))

# Modifying a dictionary
nation["Nepal"] = "Pokhara"
print("Capital of Nepal is " + nation["Nepal"])

# Length of dictionary
print(len(nation))

# Displaying keys and values
print(nation.keys())
print(nation.values())

