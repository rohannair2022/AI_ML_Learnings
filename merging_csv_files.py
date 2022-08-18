# The final file will appear along with the Folder file

import pandas as pd
import os

df = pd.read_csv('./Folder/File.csv')
files = [file for file in os.listdr('./Folder')] #Folder should contain all the csv files u want to merge 

merged_data = pd.DataFrame()
for file in files:
  df = pd.read_csv("./Folder/"+file)
  merged_data = pd.concat([merged_data, df])
  
merged_data.head()
  
