#grades. csv includes grades of 12 kids

folder = "C:\\Users\\Rohans PC\\OneDrive\\Desktop\\"
import pandas as pd
grades = pd.read_csv(folder + 'grades.csv')
a = grades.head()
print(a)
