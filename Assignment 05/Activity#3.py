def get_name():
    name = str(input("Enter the employee's Last Name: "))

    return name


def get_hours():
    hours = float(input("Enter the number of hours worked in a week: "))

    return hours


def get_rate():
    rate = float(input("Enter the rate of pay for the employee: "))

    return rate


def calculate_overtime(hours, rate):
    if hours > 40:
        overtime = (hours - 40) * (rate * 1.5)
    else:
        overtime = 0

    return overtime


def calculate_pay(rate, hours, overtime):
    pay = (((rate * hours)) + overtime)

    return pay


def display_results(name, hours, rate, pay):
    print (name, " worked ", hours, "hours in a week")
    print (str(name) + "'s hourly rate is $", rate)
    print (str(name) + "'s total gross pay is: ", pay)


def main():
    name = get_name()
    hours = get_hours()
    rate = get_rate()
    overtime = calculate_overtime(hours, rate)
    pay = calculate_pay(rate, hours, overtime)
    display_results(name, hours, rate, pay)


#Main
#This program the name and total gross pay for a user
main()