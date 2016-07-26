# String Manipulation Example

# String Formatting
print("%c is my favourite character and %s is my favourite string, %d is my favourite integer and %.5f is my favourite float number" % ("A", "Hello", 1, 3.141596))

# String Manipulation
long_string = "what is my name ?"

print(long_string.capitalize())

print(long_string.find("name"))

# Is everything letter
print(long_string.isalpha())
# Is everything number
print(long_string.isalnum())

print(len(long_string))

print(long_string.replace("name", "age"))

# Stripping white spaces
print(long_string.strip())

new_list = long_string.split(" ")
print(new_list)