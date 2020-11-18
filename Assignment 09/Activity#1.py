def display_order(names):
    print (names)


def display_reverse(names):
    names.reverse()
    print (names)


def main():
    names = ["Razzak", "Umer", "Humza", "Yousuf", "Amin",
             "Naheed", "Paryani", "Sana", "Adnan", "Marium"]
    display_order(names)
    display_reverse(names)

# Main
# This program displays list of names in order and reverse.
main()
