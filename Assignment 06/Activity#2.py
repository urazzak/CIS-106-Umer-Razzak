def get_quantity():
    quantity = int(input("Enter the quantity of items ordered: "))

    return quantity


def calculate_price(quantity):
    if quantity > 1000:
        price = 8.00
    if quantity >= 500:
        price = 10.00
    else:
        price = 12.00

    return price


def calculate_total(quantity, price):
    total = price * quantity

    return total


def display_results(quantity, price, total):
    print ("The quantity of items ordered is: ", quantity,
           ", the price per items is: $", price,
           ", and the total price is: $", total)


def main():
    quantity = get_quantity()
    price = calculate_price(quantity)
    total = calculate_total(quantity, price)
    display_results(quantity, price, total)


# Main
# This program prompts user for qunatity and calculates total price
main()
