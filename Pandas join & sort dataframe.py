# # Pandas join & sort dataframe

# import pandas,numpy
# import pandas as pd

# list1 = list(map(int,input("Enter the elements : ").split()))
# df1 = pd.DataFrame(list1)
# print(df1)
# print(df1.sort_values(0)) # sort values by column


number = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34] 
 
for i in range(len(number)): 
    for j in range(i + 1, len(number)): 
 
        if number[i] > number[j]: 
           number[i], number[j] = number[j], number[i] 
 
print (number) 