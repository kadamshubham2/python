import my_module
import sys

sys.path.append(r'd:\\python_learn')

courses = ['history', 'geo', 'math']

index = my_module.find_index(courses, 'math')
# print(index)


print(sys.path)