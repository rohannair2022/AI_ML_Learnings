folder = "C:\\Users\\Rohans PC\\OneDrive\\Desktop\\" 
import pandas as pd
grades = pd.read_csv(folder + 'grades.csv')
grades.sort_values(['column_name'], ascending = True) # sorts the data according to the ascending order of the column given 
