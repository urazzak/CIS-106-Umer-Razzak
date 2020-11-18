def display_order(names, scores):
    for index in range(len(names)):
        for index in range(len(scores)):
            print (names[index], " recieved ", scores[index], "%")


def main():
    names = ["Razzak", "Umer", "Humza", "Yousuf", "Amin",
             "Naheed", "Paryani", "Sana", "Adnan", "Marium"]
    scores = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
    display_order(names, scores)

# Main
# This program displays list of names in order and reverse.
main()
