folder = "C:\\Users\\Rohans PC\\OneDrive\\Desktop\\" #path address of the file should always have double slash
import pandas as pd
grades = pd.read_csv(folder + 'grades.csv')
grades.head() #used to display contents of the CSV file 