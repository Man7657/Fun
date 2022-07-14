# import random
# age=list(random.randint(30,70,100))
# print(age)

import random
import pandas as pd

age_list=[]
for i in range(0,100):
    n=random.randint(30,70)
    age_list.append(n)
gender_list=[]
for i in range(0,100):
    n=random.randint(1,3)
    if n==1:
        gender_list.append("M")
    else:
        gender_list.append("F")
        
Blood_level=[]
for i in range(0,100):
    n=random.randint(100,3000)
    Blood_level.append(n)
    
data={"AGE":age_list,"GENDER":gender_list,"BLOOD LEVEL":Blood_level}
df=pd.DataFrame(data)
print(data)
