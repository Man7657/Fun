# str1 = "nizamabad"
# str2 = ""
# for i in str1:
#     str2 = i + str2
# print(str2)

# from PIL import Image
#
# im = Image.open(r"C:\Users\aslam\OneDrive\Pictures\HELPLINE.jpg")
# im.show()
# im = im.rotate(180)
# im.show()

# string = "python"
# for i in string:
#     #print(i)
#     print(i[len(i)-2],end=" ")

# num = input("Enter values : ").split()
# stri = "".join(num)
# print(num, stri)


# print(type(2))
# print(type('s'))

import numpy as np

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmax(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

print(selection_sort([2,5,8,4,6]))