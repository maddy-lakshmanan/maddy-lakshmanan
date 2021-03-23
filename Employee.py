class Dummy:
    pass

# This class teaches you class variables, print namespace, class methods

class Employee:
    raise_amount = 1.04 #class variables
    num_of_employees = 0 # class variable to track the number of employees

    def __init__(self, firstName, lastName,pay):
        self.firstName=firstName
        self.lastName=lastName
        self.pay=pay
        Employee.num_of_employees += 1;

    def fullName(self):
        return '{} {} '.format(self.firstName,self.lastName)

    def apply_raise(self):
        self.pay = self.pay * Employee.raise_amount #When calling class variable, use class name

emp1 = Employee('Maddy','Lakshmanan',200000)
emp2 = Employee('Divya', 'Maddy',200000)



print(emp1.fullName())
print(Employee.fullName(emp1)) #Another way to invoke a object method

emp1.apply_raise()
print(emp1.__dict__) #This is similar to toString method in java. It prints the entire dictionary of the object

print("Number of employees -" , Employee.num_of_employees);
        