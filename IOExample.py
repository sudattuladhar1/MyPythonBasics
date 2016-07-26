# IO Example
import sys
import os

# Write to a file
test_file = open("test.txt", "wb")

print(test_file.mode)
test_file.write(bytes("Write me to the file\n", 'UTF-8'))

test_file.close()


# Read from a file
test_file = open("test.txt", "r+")

print(test_file.mode)
my_text = test_file.read()
print(my_text)

test_file.close()

# Delete the file
# os.remove("test.txt")