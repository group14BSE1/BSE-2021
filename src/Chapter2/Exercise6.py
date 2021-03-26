# Prompt user for the first point
x_1 = input("Enter x1:")
# Prompt user for the first point
y_1 = input("Enter y1:")
# Prompt user for the first point
x_2 = input("Enter x2:")
# Prompt user for the first point
y_2 = input("Enter y2:")

# calculate difference between the x coordinates
first_diff = int(x_2) - int(x_1)

# calculate difference between the y coordinates
second_diff = int(y_2) - int(y_1)

# Sum the squares of the differences
square_result = first_diff**2 + second_diff**2

# attain square root by raising to power a half
distance = square_result**(1/2)

print("The difference between the two points is:", distance)


