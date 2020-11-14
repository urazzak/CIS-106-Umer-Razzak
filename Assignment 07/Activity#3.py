def get_consent():
    consent = str(input("Input 'Yes' to continue with the program: "))

    return consent


def get_name():
    name = str(input("Enter the students last name: "))

    return name


def calculate_average():
    score = float(input("Enter the students first score: "))
    grade = float(input("Enter the students second score: "))
    average = (score + grade) / 2

    return average

def display_results():
    consent = get_consent()
    while consent == 'Yes' or consent == 'yes':
        name = get_name()
        average = calculate_average()
        print (name, "'s average score is: ", average, "%")
        consent = get_consent()


def main():
    display_results()


# Main
# This program calculates and displays student's average.
main()
