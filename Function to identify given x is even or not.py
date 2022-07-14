#Function to identify given x is even or not

n = int(input("Enter your number : "))


def even_or_not(num):
    if num % 2 == 0:
        print(" {} is Even number".format(num))
    else:
        print(" {} is Odd number".format(num))


even_or_not(n)

# n = int(input("Enter n value: "))
# for i in range(1,2*n):
#     if i <= n:
#         print('*'*i)
#     elif i>n:
#         print('*'*(2*n-i))