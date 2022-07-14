# Function to multiply elements of list by 10

lst = list(map(int, input("Enter the elements of list : ").split()))

print(lst)
def multiply_list(input_list):
    new_list = [10*x for x in input_list]
    print(new_list)


multiply_list(lst)
print(lst.pop(2))
print(lst.remove(4))
print(lst)
