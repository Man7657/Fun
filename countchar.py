# st = input("Enter the sequence : ")
# for i in range(len(st)):
#   st = st[i+1:]
#   f_s = st[i]
#   count = 0
#   for i in range(len(st)):
#     if st[i] == f_s:
#       count += 1
#       if st[i] == st[i+1]:
#         continue
#       else:
#         break
#   c = str(count)
#   print(f_s+c,end="")

# st = input("Enter the sequence : ")
# for x in range(len(st)):
#   if st != "":
#     f_s = st[0]
#     count = 0
#     for i in range(len(st)):
#       if st[i] == f_s:
#         count += 1
#         try:
#             if st[i] == st[i+1]:
#               continue
#             else:
#               break
#         except IndexError:
#           pass
#     st = st[i+1:]
#     c = str(count)
#     print(f_s+c,end="")
#   else:
#     break
#
# s="hello world"
# t=list()
# for i in list(set(s)):
#   c=0
#   for j in s:
#     if i==j:
#       c+=1
#     d[i]=c
# print(d)

#
# s1="karthik"
# s2="thrikak"
# l1=list(s1)
# l2=list(s2)
# if (l1.sort()==l2.sort()):
#   print("yes")
#
# else:
#   print("no")
#

# from audioop import reverse


s="suneel is a good boy"
# b=reversed(s)
# print(''.join(b))
#  print(''.join(reversed(s)))
# print(s[::-1])
b=''
for i in s:
    b=i+b
print(b) 