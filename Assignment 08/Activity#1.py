def get_amount():
    amount = float(input("Enter the amount invested in a CD: "))

    return amount


def get_rate():
    rate = float(input("Enter the applied Interest Rate: "))

    return rate


def get_term():
    term = (input("Enter the years of the Term: "))

    return term


def calculate_simple(amount, rate):
    simple = amount * rate 

    return simple

def display_results():
    amount = get_amount()
    rate = get_rate()
    term = get_term()
    year = 1
    for year in range(year, int(term) + 1, 1):
        simple = calculate_simple(amount, rate)
        amount = amount + simple
        print ("For year", year, " the interest is ", simple, " and the total is ", amount)

def main():
    display_results()

# Main
# This program calculates simple interest by year.
main()
