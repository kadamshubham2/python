try:
    f = open('test.txt', 'r')
except FileNotFoundError as e:
    print("File not found:", e)
    var = bad_var
except Exception as e:
    print("Other exception:", e)


