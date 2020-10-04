# This program will help users determine how much paint is required for the room and cost.
# Prompt user to input length, width and hieght of room.
# Prompt user to input price per gallon of paint.
print("Enter the length of the room in feet")
length = float(input())
print("Enter the width of the room in feet")
width = float(input())
print("Enter the height of the room in feet")
height = float(input())
print("Enter the price per gallon of paint")
price = float(input())

# Calculate the area of the room, total number of gallons needed, and total cost.
area = 2 * length * height + 2 * width * height
gallons = area / 400
cost = gallons * price

# Display Results: Display total gallons and total cost
print("The amount of paint required is " + str(gallons) + ", the total cost is $" + str(cost))
