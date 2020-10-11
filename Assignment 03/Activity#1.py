def displayHello(name):
    print("Hello " + name + "!")

def getName():
    print("What is your name?")
    name = input()
    
    return name

# Main
name = getName()
displayHello(name)
