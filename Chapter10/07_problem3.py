class demo:
    a = 4

o = demo()
print(o.a)

o.a = 0
print(o.a)
print(demo.a)

# Prints the class attribute because instance attribute is not present
o.a = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute because instance attribute is present
print(demo.a) # Prints the class attribute