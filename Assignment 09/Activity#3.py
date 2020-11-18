def get_maximum(names, scores):
    for index in range(len(names)) and range(len(scores)):
            maximum = scores[0]
            if maximum < scores[index]:
                maximum = "highest score is", scores[index], "by", names[index]
    
    return maximum


def get_minimum(names, scores):
    for index in range(len(names)) and range(len(scores)):
        minimum = scores[0]
        if minimum >= scores[index]:
            minimum = "lowest score is ", scores[index], "by", names[index]
    
        return minimum


def get_average(scores):
    average = sum(scores) / len(scores)

    return average



def main():
    names = ["Razzak", "Umer", "Humza", "Yousuf", "Amin",
             "Naheed", "Paryani", "Sana", "Adnan", "Marium"]
    scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    maximum = get_maximum(names, scores)
    minimum = get_minimum(names, scores)
    average = get_average(scores)
    print (maximum)
    print (minimum)
    print ("and the average score is ", average)


# Main
# This program displays list of names in order and reverse.
main()
