nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('found')
        break
    print(num)

for num in nums:
    if num == 3:
        print('found')
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        break
        # print(num, letter)

x = 0
while x < 10:
    print(x)
    x += 1

while True:
    if x == 5:
        break
    print(x)
    x += 1
