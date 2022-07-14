# *Check given number is armstrong or not*
num = int(input("Enter your choice of number : "))
st_num = str(num)
n = len(st_num)
count = 0
for i in st_num:
    count = count + (int(i))**n
if count == num:
    print("Given number is Armstrong number")
else:
    print("Given number is not Armstrong number")

# *Check given number is palindrome or not*
num = int(input("Enter your choice of number : "))
dup_num = num
rev_num = 0
while num != 0:
    temp = num % 10
    rev_num = rev_num * 10 + temp
    num = num // 10
if rev_num == dup_num:
    print("Given number is Palindrome number")
else:
    print("Given number is not Palindrome number")

# *Check given number is perfect or not*
num = int(input("Enter your choice of number : "))
count = 0
for i in range(1, num):
    if num % i == 0:
        count = count + i
    else:
        continue
if count == num:
    print("Given number is Perfect number")
else:
    print("Given number is not Perfect number")

# *Display primes upto given number using nested while loop*
num = int(input("Enter your choice of number : "))
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
