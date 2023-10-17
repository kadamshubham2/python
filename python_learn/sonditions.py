user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('welcome')
else:
    print('sorry')

if user == 'admin' or logged_in:
    print('welcome')
else:
    print('sorry')

logged_in = False

if not logged_in:
    print('please log in')
else:
    print('sorry')

a = 123
b = 456
print(id(a))
print(id(b))
print(a is b)

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')