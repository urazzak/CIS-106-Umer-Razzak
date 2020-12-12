class Employee:
    empcount = 0 

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        Employee.empcount += 1
    
    def displayEmployee(self):
      print ("First Name: ", self.firstname, " Last Name: ", self.lastname,  ", Salary: $", self.salary)


emp1 = Employee(input("Enter the First Name: "),
                input("Enter the Last Name: "), (input("Enter salary: ")))
emp1.displayEmployee()
