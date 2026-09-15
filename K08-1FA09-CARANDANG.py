import math

# Get the coordinates of the first point from the user.
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Get the coordinates of the second point from the user.
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the difference between the x-coordinates and y-coordinates.
x_difference = x2 - x1
y_difference = y2 - y1

# Calculate the distance using the distance formula.
distance = math.sqrt(
    math.pow(x_difference, 2) + math.pow(y_difference, 2)
)

# Display the calculated distance rounded to two decimal places.
print(f"\nThe distance between the two points is: {distance:.2f}")