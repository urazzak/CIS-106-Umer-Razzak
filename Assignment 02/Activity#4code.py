# This program converts gallons to liters
# Prompt user for volume in gallons
print("Enter the amount of gallons: ")
gallons = float(input())

# Convert gallons into liters (metric conversion)
liters = gallons * 3.7854

# Display Results: display converted volume
print("The volume in liters is " + str(liters))
