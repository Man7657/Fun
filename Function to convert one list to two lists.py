# Function to convert one list to two lists

main_list = [int(elem) for elem in input("Enter the elements of list : ").split()]


def divide_list(ml):
    el = list(filter((lambda x: x % 2 == 0), ml))
    ol = list(filter((lambda x: x % 2 != 0), ml))
    print("Even List : ", el)
    print("Odd List : ", ol)


divide_list(main_list)
