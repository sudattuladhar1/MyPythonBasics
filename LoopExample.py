# Loop Example
import random

for i in range(0,10):
    print(i, ' ', end="" )

print("\r")

grocery_list = ["fruits", "vegetables", "juice", "Milk", "Meat"]

for item in grocery_list:
    print(item," ", end="")

print("\r")

number_list = [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]]

for x in range(0,3):
    for y in range(0,4):
        print(number_list[x][y], " ", end="")
    print("\r")

rand = random.randrange(0,100)

while(rand != 15):
    print(rand, " ", end="")
    rand = random.randrange(0,100)

print("\nTarget Hit !!! ", rand)