import pandas as pd
import numpy as np
import openpyxl,lxml

df = pd.read_csv(r"C:\Users\aslam\Downloads\mydata\data3.csv")
#print(df)
print(df["Period"])
print(np.median(df["Data_value"]))
print(np.average(df["Data_value"]))
print(df["Period"][:4])

