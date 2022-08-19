folder = "C:\\Users\\Rohans PC\\OneDrive\\Desktop\\" 
import pandas as pd
grades = pd.read_csv(folder + 'grades.csv')
grades.sort_values(['column_name'], ascending = True) # sorts the data according to the ascending order of the column given 
grades.groupby(['column_name_1']).mean().sort_values('coulmn_name_2', ascending = False) # sort data based on the mean value of a certain column 
grades.groupby(['column_name']).mean() #displays all the mean data accoding to data in a certain column

df['count'] = 1
grades.groupby(['column_name'].count()['count']) # used to count each item in a particular column
grades.groupby(['column_name1','column_name2'].count()['count']) #used to count each item in a particular column with respect to the other column as well
         
