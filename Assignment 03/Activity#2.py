def calculateArea(length, width):
    area = length * width
    
    return area

def calculatePerimeter(length, width):
    perimeter = 2 * length + 2 * width
    
    return perimeter

def displayResults(area, perimeter):
    print("The Area of the room is " + str(area) + ", and the Perimeter is " + str(perimeter))

def getLength():
    print("Enter the length of the room in feet:")
    length = float(input())
    
    return length

def getWidth():
    print("Enter the width of the room in feet:")
    width = float(input())
    
    return width

# Main
# This program will calculate the area and perimeter of a room
length = getLength()
width = getWidth()
area = calculateArea(length, width)
perimeter = calculatePerimeter(length, width)
displayResults(area, perimeter)
