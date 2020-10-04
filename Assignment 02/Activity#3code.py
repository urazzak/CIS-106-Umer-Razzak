print("Place bag or jar of coins on the counter")
print("Enter the amount of qaurters: ")
quarters = int(input())
print("Enter the amount of dimes: ")
dimes = int(input())
print("Enter the amount of nickels: ")
nickels = int(input())
print("Enter the amount of pennies: ")
pennies = int(input())
quarter = 0.25
dime = 0.1
nickel = 0.05
penny = 0.01
total = nickels * nickel + quarters * quarter + dimes * dime + pennies * penny
print("Your total amount is: $" + str(total))
