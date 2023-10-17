student = {"shubham": "25", "age": "23", "sub": ['maths', 'sci']}

print(student)
print(student['sub'])
print(student.get('volt'))
print(student.get('volt', 'not found'))
student["num"] = 555555
print(student)
student.update({'name': "jane", 'age': 30})
print(student)

pop_list = student.pop('age')
print(pop_list)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

# for key in student.keys():
#     print(key)

for key, value in student.items():
    print(key, value)