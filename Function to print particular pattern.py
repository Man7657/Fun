# # Function to print particular pattern
#
# num = int(input("Enter the longest length : "))
#
#
# def pattern(n):
#     for i in range(1, 2*n+1):
#         if i <= n:
#             print("*"*i)
#         else:
#             print("*"*(2*n-i))


pattern(num)

# class TeamMember(object):
#     def __init__(self, name, uid):
#         self.name = name
#         self.uid = uid
#
# # Parent class 2
# class Worker(object):
#     def __init__(self, pay, jobtitle):
#         self.pay = pay
#         self.jobtitle = jobtitle
#
# # Deriving a child class from the two parent classes
# class TeamLeader(TeamMember, Worker):
#     def __init__(self, name, uid, pay, jobtitle, exp):
#         self.exp = exp
#         TeamMember.__init__(self, name, uid)
#         #Worker.__init__(self, pay, jobtitle)
#         print("Name: {}, Pay: {}, Exp: {}".format(
#             self.name, self.pay, self.exp))
#
#
# TL = TeamLeader('Michael', 10001, 250000, 'Scrum Master', 5)