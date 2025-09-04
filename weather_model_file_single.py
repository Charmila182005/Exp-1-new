import math

# Read input values from file
with open("input_single.txt", "r") as file:
    a, b, c = map(float, file.readline().split())

# Calculate discriminant
D = b**2 - 4*a*c

# Compute roots
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Two real roots: {x1}, {x2}")
elif D == 0:
    x = -b / (2*a)
    print(f"One real root: {x}")
else:
    print("No real roots")
