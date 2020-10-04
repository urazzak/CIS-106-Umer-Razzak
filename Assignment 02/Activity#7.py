# This program  prompts the user for the name of their dog and its age in human years. Then convert it into dog years.
print("Enter your dog's name.")
name = input()
print("Enter your dag's age in years.")
age = float(input())
dogyears = age * 7
print(name + " is currently " + str(dogyears) + " years old in dog years")
