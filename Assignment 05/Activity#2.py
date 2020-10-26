def get_widget():
    widget = (input("Enter widget A or B: "))

    return widget


def get_quantity():
    quantity = int(input("Enter the quantity of widgets: "))

    return quantity


def calculate_price(widget):
    if widget == "A" or widget == "a":
        price = 10
    else:
        if widget == "B" or widget == "b":
            price = 20
        else:
            print ("You did not make a correct selection")
    
    return price


def calculate_total(price, quantity):
    total = float(price) * int(quantity)

    return total


def display_results(widget, price, total):
    print ("The wideget is: ", widget)
    print ("The price of widget", widget, " is $", float(price))
    print ("The total cost is ", total) 


def main():
    widget = get_widget()
    price = calculate_price(widget)
    quantity = get_quantity()
    total = calculate_total(price, quantity)
    display_results(widget, price, total)

#Main
#This program calculates and displays total cost of order based of widget price
main()