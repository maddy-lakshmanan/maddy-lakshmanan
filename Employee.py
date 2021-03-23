class Dummy:
    pass

class Employee:
    def __init__(self, firstName, lastName,pay):
        self.firstName=firstName
        self.lastName=lastName
        self.pay=pay

    def fullName(self):
        return '{} {} '.format(self.firstName,self.lastName)
    
emp1 = Employee('Maddy','Lakshmanan','200k')
emp2 = Employee('Divya', 'Maddy','200k')

print(emp1.fullName())
        