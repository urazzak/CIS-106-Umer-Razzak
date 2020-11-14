def get_name():
    name = input("Enter the employees last name: ")
    
    return name


def get_code():
    code = input("Enter job code A or B: ")

    return code


def get_years():
    years = int(input("Enter the the years of service of the employee: "))

    return years


def calculate_bonus(code, years):
    if (code == 'A' or code == 'a') and years > 10:
        bonus = "10,000"
    else:
        if code == 'A' or code == 'a' and years >= 5:
            bonus = "8,000"
        else:
            if code == 'B' or code == 'b' and years > 15:
                bonus = "9,000"
            else:
                bonus = "5,000"

    return bonus


def display_results(name, code, years, bonus):
    print (name, "will receive $", str(bonus), " as their bonus")


def main():
    name = get_name()
    code = get_code()
    years = get_years()
    bonus = calculate_bonus(code, years)
    display_results(name, code, years, bonus)


# Main
# This program will calculate and display employee's bonus
main()