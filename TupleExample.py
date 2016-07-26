# Tuple Example

pi_tuple = (3, 1, 4, 1, 5, 9, 6)

print(pi_tuple)
print(pi_tuple[0:3])

# Can't change the tuple directly as : pi_tuple[1] = 4

# Converting tuple elements using list
newlist = list(pi_tuple)
newlist[1] = 4
new_tuple = tuple(newlist)

print(new_tuple)