#Program for factorial of a no. using function:
def fact(n):
  fact=1
  for i in range (1,n+1):
    if i<=n:
      fact=fact*i
  print (fact)
n=int(input("enter any no:"))
(fact(n))




