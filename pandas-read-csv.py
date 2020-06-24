import pandas as pd # {pip install pandas} for use pandas
# Read data from file 'filename.csv' 
data = pd.read_csv("csv\\aliexpresstest.csv") 

#data_dict = data.to_dict('series')
#data_dict = data.to_dict('dataframe')

print(data.loc[[2]])
