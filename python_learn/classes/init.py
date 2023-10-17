
class Employee():       
    
        def __init__(self, first, last, pay):
                self.first = first#instance variables
                self.last = last
                self.pay = pay

        def fullname(self):
                print(f"{self.first} {self.last}")

emp_1 = Employee()
emp_2 = Employee()# here Employee() is class and emp_1 and emp_2 is instances of class

# emp_1.first = 'shubham'
# emp_1.last = 'kadam' #.first and .last are instance variavbles

emp_1 = Employee('shubham', 'kadam', 20000)
emp_2 = Employee('s', 'kadam', 20000)

print(emp_1.fullname())


