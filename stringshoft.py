# Given two strings A and B, write a function can_shift to return whether
# or not A can be shifted some number of places to get B.
#
# Example:
#
# A = 'abcde'
# B = 'cdeab'
# can_shift(A, B) == True
#
# A = 'abc'
# B = 'acb'
# can_shift(A, B) == False


A = input("Enter the string A : ")
B = input("Enter the string B : ")
def can_shift(A,B):
    count = 0
    for i in range(len(B)):
        shift_str = B[i:] + B[:i]
        if A == shift_str:
            count += 1
        else:
            pass
    if count != 0:
        print(True)
    else:
        print(False)

can_shift(A,B)

