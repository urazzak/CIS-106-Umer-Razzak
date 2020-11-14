def displayAward(years):
    if years > 10:
        print("The employees Service Award is $1,000")
    else:
        if years >= 5:
            print("The employee's Service Award is $500.00")
        else:
            if years < 5:
                print("The employee's Service Award is $100.00")
            else:
                print("You did not enter a valid input")

def getInput():
    print("Enter employee's year(s) of service")
    years = int(input())
    
    return years

# Main
years = getInput()
displayAward(years)
