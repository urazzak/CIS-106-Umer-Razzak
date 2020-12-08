def get_name():
    name = str(input("Enter your first and last name: "))

    return name


def split_name(name):
    split = name.split()

    return split


def display_results(name, split):
    print ("{},".format(split[1]), "{}.".format(name[0]))


def main():
    name = get_name()
    split = split_name(name)
    display_results(name, split)


# Main
# This program prompts user for name and display it back
main()
