num = int(input("Enter the range of number :"))
# if num > 1:
#     for n in range(2,num+1):
#         for i in range(2,n):
#             if n % i == 0:
#                 break
#         else:
#             print(n,end=" ")
# else:
#     print("Enter number greater than 1")

if num > 1:
    n = 1
    while n < num+1:
        count = 0
        i = 2
        while i < n:
            if n % i == 0:
                count = count + 1
                break
            i = i+1

        if count==0 and n != 1:
            print(n,end=" ")
        n = n+1
