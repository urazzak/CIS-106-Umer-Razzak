def get_input(array):
    for index in range(len(array)):
        array[index] = input("Enter a value: ")


def display_results(array):
    for index in range(len(array)):
        print(array[index])


def main():
    array = [None] * 3
    get_input(array)
    display_results(array)

# Main
# This Program creates a dynamic array
main()
