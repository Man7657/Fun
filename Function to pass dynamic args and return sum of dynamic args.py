# Function to pass dynamic args and return sum of dynamic args

values = list(map(int, input("Enter the elements : ").split()))


def addition(*args):
    s = 0
    for x in args:
        s += x
    print("Sum of given dynamic elements : ", s)


addition(*values)