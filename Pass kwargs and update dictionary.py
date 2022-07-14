# # Pass kwargs and update dictionary
#
# def keyword_arg(**kwargs):
#     print(kwargs)
#
#
# dict1 = {'abc': 3, 'defg': 4}
#
# keyword_arg(**dict1)
# keyword_arg(para2=3, **dict1)

# import pandas as pd
# d = {"rollno": [1,2,3,4,5],
#      "name":['J','K','L','M','N'],
#         "marks":[90,80,98,78,89]}
# # i = int(input())
# # print(d['name'][i] , d["marks"][i])
#
# df = pd.DataFrame(d)
# print(sum(df['rollno']))
# print(df.iloc[df[df['rollno'] == 4].index.values])
