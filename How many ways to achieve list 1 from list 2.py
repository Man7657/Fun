# How many ways to achieve list 1 from list 2

list1 = list(map(int,input("Enter the elements : ").split()))
n = int(input("Enter the index value to element to remove : "))

print(list1.pop(n))
print(list1[:n]+list1[n+1:])


