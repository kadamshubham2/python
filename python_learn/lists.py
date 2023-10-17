# lists and tuples usually used for sequential data

data = ['history', 'science']
data1 = ['maths', 'edu']

data.append("art")
print(data)
data.insert((0, 1, 2, 3), ["data", 'b', 'c', 'd'])
print(data)
# data.extend(data1)
# print(data)
# data.remove('maths')
# print(data)
# popped = data.pop()

# data.reverse()
# print(data)
# data.sort()
# print(data)

# sorted_list = sorted(data)
# print(sorted_list)
# number = [1, 2, 3, 4, 5]
# print(min(number))
# print(max(number))
# print(data.index("data"))

# print("art" in data)
# print("no" not in data)

# for item in data:
#     print(item)

# for index, value in enumerate(data):
#     print(index, value)

# for index, value in enumerate(data, start=1):
#     print(index, value)

# course_str = " - ".join(data)
# print(course_str)

# course_spl = course_str.split("-")
# print(course_spl)