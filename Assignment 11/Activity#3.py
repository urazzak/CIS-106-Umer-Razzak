def get_value():
    value = input("Enter test scores: ")

    return value


def split_string(value):
    split = value.split(',')

    return split


def display_results(value, split):
    index = 0
    for index in range(len(value)):
        print ("{}".format(split[index].strip(' ')))


def main():
    value = get_value()
    split = split_string(value)
    display_results(value, split)


# Main
# This Program prompts user for scores and displays scores
main()
