# Convert string to list and again revert back

def str_to_list(string1):
    list1 = list(string1)
    print("Given string to list : ", list1)

    def list_to_str(lst):
        string2 = "".join(list1)
        print("Back to String : ", string2)

    list_to_str(list1)


str_to_list(input("Enter the word : "))