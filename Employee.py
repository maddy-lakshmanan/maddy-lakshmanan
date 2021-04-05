class Dummy:
    pass

# This class teaches you class variables, print namespace, class and static methods
# We generally use class method to create factory methods. Factory methods return class object ( similar to a constructor ) 
# for different use cases.
# We generally use static methods to create utility functions.

class Employee:
    raise_amount = 1.04 #class variables
    num_of_employees = 0 # class variable to track the number of employees

    def __init__(self, firstName, lastName,pay):
        self.firstName=firstName
        self.lastName=lastName
        self.pay=pay
        Employee.num_of_employees += 1;

    def __del__(self):
      # body of destructor
      print("Destructor called",self)

    def fullName(self):
        return '{} {} '.format(self.firstName,self.lastName)

    def apply_raise(self):
        self.pay = self.pay * Employee.raise_amount #When calling class variable, use class name
    
    @classmethod
    def update_raise(cls, amount): #Note we need to pass cls instead of self 
        cls.raise_amount=amount

    #you can use class method as constructor or factory 
    @classmethod
    def from_emp_string(cls, emp_string):
        firstName,lastName,pay = emp_string.split('-')
        return cls(firstName,lastName,pay)
    
    #staticmethod    
    def isHighPaid(pay):
        if(pay>50000):
            return True

class Developer(Employee):
    def __init__(self,firstName,lastName,pay,program):
        super().__init__(firstName,lastName,pay)
        self.program = program    
class Manager(Employee):
    def __init__(self,firstName,lastName,pay,employees=None):
        super().__init__(firstName,lastName,pay)
        self.employees = employees
    # def add_emp   

emp1 = Employee('Maddy','Lakshmanan',200000)
emp2 = Employee('Divya', 'Maddy',200000)
# calling class method to create constructor
emp3 = Employee.from_emp_string('Nivedha-Maddy-500000')
dev1 = Developer('Maya','Maddy',500000,'Java')

# print(emp1.fullName())
# print(Employee.fullName(emp1)) #Another way to invoke a object method

# emp1.apply_raise()
# print(emp1.__dict__) #This is similar to toString method in java. It prints the entire dictionary of the object

# print("Number of employees -" , Employee.num_of_employees);

# #calling class method
# Employee.update_raise(1.05)
# emp2.apply_raise()
# print(emp2.__dict__)

# print(emp3.fullName())

# #calling static method
# print(Employee.isHighPaid(emp1.pay))

# calling parent constructor
print(dev1.fullName())
        