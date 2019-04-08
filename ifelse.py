print("Learning if/else/elif in python")
x = 10
y = 20
z = 5

# type 1

if x < y:
    print("x is less than y")
else:
    print("x is greater than y")

# type 2
if x < z:
    print("x is less than z")
elif x > z:
    print("x is greater than z")
else:
    print("x is equal to z")

# type 3

name = "Chandan"

if name == "Chandan":
    print("Welcome "+name)
else:
    print("Name please?")

