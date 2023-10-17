list = [7,4,3,5,9,1]
from operator import attrgetter
# sort_list = sorted(list)
# print(sort_list)

# list.sort()
# print(list)
#sort() method only works with list
#sorted function works with any iterable

# list = [-5, -6, -7, 2, 3, 4, 1]
# n_list = sorted(list, key=abs)
# print(n_list)

class employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name} {self.age} {self.salary}"
    

employee1 = employee("John Doe", 30, 50000)
employee2 = employee("Johny Doe", 40, 40000)
employee3 = employee("J Doe", 45, 60000)
employees = [employee1, employee2, employee3]

def e_sort(emp):
    return emp.salary

# s_employees = sorted(employees, key=e_sort, reverse=True)
# s_employees = sorted(employees, key=lambda e: e.age)
s_employees = sorted(employees, key=attrgetter('age'))
print(s_employees)

# The __repr__ method in a Python class is used to define a string 
# representation of an object. It should return a string that, when 
# evaluated, should ideally create an object with the same state as 
# the original object. It is mainly used for debugging and development 
# purposes, providing a human-readable and unambiguous representation of an object.

