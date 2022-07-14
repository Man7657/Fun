# Function to print factorial of given number

num = int(input("Enter the required number : "))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(num))
