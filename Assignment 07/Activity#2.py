def get_start():
    start = float(input("Enter the Starting Value for the counter: "))

    return start


def get_stop():
    stop = float(input("Enter the Stopping Value for the counter: "))

    return stop


def get_increment():
    increment = float(input("Enter the value you would like to increment by: "))

    return increment


def display_results(start, stop, increment):
    while start <= stop:
        print (start)
        start = start + increment


def main():
    start = get_start()
    stop = get_stop()
    increment = get_increment()
    display_results(start, stop, increment)


# Main
# This program counts based off user's inputs
main()