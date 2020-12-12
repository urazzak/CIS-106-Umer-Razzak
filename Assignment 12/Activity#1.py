def get_data():
    datafile = open("/Users/umerrazzak/Desktop/School/"
                    "CIS-106/Assignment 12/scores.txt")

    return datafile


def split_file(datafile):
    scores = []
    line = datafile.readline()
    while True:
        line = datafile.readline()
        if not line:
            break
        split = line.split(",")
        scores.append(int(split[1].strip('\n')))

    return scores


def calculate_average(scores):
    total = 0
    for index in range(len(scores)):
        total += scores[index]
        average = total / len(scores)

    return average


def get_max(scores):
    maximum = scores[0]
    for index in range(1, len(scores)):
        if maximum < scores[index]:
            maximum = scores[index]

    return maximum


def get_min(scores):
    minimum = scores[0]
    for index in range(1, len(scores)):
        if minimum > scores[index]:
            minimum = scores[index]

    return minimum


def display_results(scores, average, maximum, minimum):
    print ("The classes scores are: ", scores)
    print ("The average score is: ", round(average, 2))
    print ("The highest score is: ", maximum)
    print ("The lowest score is: ", minimum)


def main():
    datafile = get_data()
    scores = split_file(datafile)
    average = calculate_average(scores)
    maximum = get_max(scores)
    minimum = get_min(scores)
    display_results(scores, average, maximum, minimum)


# Main
# This program imports a text file and reads the data
main()
