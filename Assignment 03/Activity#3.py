def get_quantity():
    print ("Enter the number of items: ")
    quantity = int(input())

    return quantity


def get_price():
    print ("Enter the price per item: ")
    price = float(input())

    return price


def calculate_total(quantity, price):
    total = (price * quantity)

    return total


def calculate_tax(total):
    tax = (0.7 * total)

    return tax


def calculate_cost(total, tax):
    cost =  (total + tax)

    return cost


def display_results(quantity, price, total, tax, cost):
    print ("The number of items is: " + str(quantity))
    print ("The price per item is: $" + str(price))
    print ("The total price is: $" + str(total))
    print ("The amount of tax added is: $" + str(tax))
    print ("The total cost will be: $" + str(cost))

def main():
    quantity = get_quantity()
    price = get_price()
    total = calculate_total(quantity, price)
    tax = calculate_tax(total)
    cost = calculate_cost(tax, total)
    display_results(quantity, price, total, tax, cost)

#Main
#This program calculates total cost including tax from quantity and price per item
main()