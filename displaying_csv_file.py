folder = "C:\\Users\\Rohans PC\\OneDrive\\Desktop\\" #path address of the file should always have double slash
import pandas as pd
grades = pd.read_csv(folder + 'grades.csv')

grades.head() #used to display contents of the CSV file 
grades.columns #used to display the column headers
grades['column_name'] # used to show the contents of a specific column
grades.loc[grades['column_name'] = 'item'] # used to locate a certain item in a column 
grades.describe() # used to give a little statistic about the data 
