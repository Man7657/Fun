# Square of all elements in list using lambda

list1 = list(map(int,input("Enter the numbers :").split()))
list2 = list(map(lambda x:x**2,list1))
print(list2)