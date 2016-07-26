# List Example

fruits = ["Apple", "Orange", "Grape", "Banana"]
vegetable = ["Carrot", "Cauliflower", "Cabbage", "Brinjal", "Radish"]


print("List Ranging...")
print(fruits[0:3])
print(fruits[:-2])
print(fruits[-1:])


print("List within List")
food = [fruits, vegetable]
print(food)

fruits[0] = "Papaya"

print(food)

print("List Indexing..")
print(food[1][2])

print("Appeding List..")
food.append("Juice")
print(food)

print("Inserting into the list")
fruits.insert(2,"Mango")
fruits.remove("Banana")
print(food)

print("Sorting the List")
fruits.sort()
vegetable.sort()
vegetable.reverse()
print(food)

print("Len Min Max")
print(len(fruits))
print(min(fruits))
print(max(fruits))
