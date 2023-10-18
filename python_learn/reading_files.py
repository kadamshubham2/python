# with open function

# file = open('read.txt', 'r') # mode r, w, a, rb, wb)
# print(file.read())
# file.close()

#with context manager
with open('read.txt', 'r') as file:
    contents = file.read() #file.readline, file.readlines
    file.seek(0)
    print(contents, end='1')

# write mode
with open('read1.txt', 'w') as file:
    file.write('hello ')
    file.seek(6)
    file.write('how you do')