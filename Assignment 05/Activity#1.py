def calculateOrder(shipping, tax, total):
    order = total + shipping + tax
    
    return order

def calculateShipping(total):
    if total >= 100:
        shipping = 0
    else:
        shipping = total * 0.1
    
    return shipping

def calculateTax(total):
    tax = total * 0.07
    
    return tax

def displayResults(tax, total, order, shipping, quantity, price):
    print("The total quantity is: " + str(quantity) + ", The price per item is: " + str(price) + ", The shipping cost is: " + str(shipping) + ", The order total is: " + str(order))

def getTotal(quantity, price):
    total = price * quantity
    
    return total

# Main
print("Enter the quantity of items: ")
quantity = int(input())
print("Enter the price for the items: ")
price = float(input())
total = getTotal(quantity, price)
tax = calculateTax(total)
shipping = calculateShipping(total)
order = calculateOrder(total, shipping, tax)
displayResults(tax, total, order, shipping, quantity, price)
