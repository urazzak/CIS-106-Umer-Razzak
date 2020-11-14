def get_term():
    term = int(input("Enter the Term to determine your CD interest rate: "))

    return term


def calculate_interest(term):
    if term == 5 or term == 10:
        interest = "2%"
    else:
        if term < 3 or term >= 1:
            interest = "1%"
        else:
            interest = ".5%"
    
    return interest


def display_results(term, interest):
    print ("The CD's Term is ", term,
            " years, and the Interest Rate is:", interest)
    

def main():
    term = get_term()
    interest = calculate_interest(term)
    display_results(term, interest)


# Main
# This program calculates and displays interest rate.
main()