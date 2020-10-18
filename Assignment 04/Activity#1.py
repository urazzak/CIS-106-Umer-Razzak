def get_name():
    name = str(input("Enter the sutdents last name: "))

    return name


def get_score1():
    score1 = int(input("Enter the first score: "))

    return score1


def get_score2():
    score2 = int(input("Enter the second score: "))

    return score2

def calculate_exam1(score1):
    exam1 = score1 * .40

    return exam1


def calculate_exam2(score2):
    exam2 = score2 * .60

    return exam2


def calculate_total(exam1, exam2):
    total = exam1 + exam2

    return total


def dislay_results(name, total, score1, score2):
    print (str(name) + "'s Exam Scores were: " + str(score1) + ", " + str(score2) + " and the Total Score was " + str(total))


def main():
    name = get_name()
    score1 = get_score1()
    score2 = get_score2()
    exam1 = calculate_exam1(score1)
    exam2 = calculate_exam2(score2)
    total = calculate_total(exam1, exam2)
    dislay_results(name, total, score1, score2)


# This program displays total score and last name
#Main
main()