# # Function to check prime number or not
#
# def prime_or_not(n):
#     c = 0
#     for i in range(1,n):
#         if n % i == 0:
#             c += 1
#         else:
#             pass
#     if c==1:
#         print(" {} is a prime number".format(n))
#     else:
#         print(" {} is not a prime number".format(n))
#
# a=range(1,10)
# prime_or_not(a)



lower = 1
upper = 10

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)