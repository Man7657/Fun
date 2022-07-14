# Given a string str of any length, write an algorithm max_repeating to
# return which character has the longest string of continuous repetition.
#
# If two characters are tied for most continuous repetition, return the character
# whose longest continuous repetition occurs earliest in str.
#
# Example 1:
#
# str = 'aabbaaccbbbaa'
# def max_repeating(str) -> b
# Example 2:
#
stri = 'adcc ccbb bbc'
print(stri.split())
# def max_repeating(str) -> c

# str1 = input("Enter the string : ")
# set_str = set(str1)
# dict = {}
# for i in set_str:
#     c = 0
#     for j in str1:
#         if i == j:
#             c += 1
#     dict[i] = c
#
# for i,j in dict.items():
#     count = 0
#     if j == max(dict.values()):
#         print(i)
#         count += 1
#         if count ==1:
#             break
#
#
#
def rep(x):
    c_h = 0
    for i in x:
        c = 0
        for j in x:
            if i==j:
                c+=1
        if c_h < c:
            c_h = i
    print(c_h)

rep([1,2,3,2,4,3,5,1,2,1,4,1,6,1,7])