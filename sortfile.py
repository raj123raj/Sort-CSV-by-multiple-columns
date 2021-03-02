#importing pandas package 
import pandas as pandasForSortingCSV 

#read_csv method accepts the input csv file and reads into DataFrame
#Importantly let CSV files be have headers 
csvData=pandasForSortingCSV.read_csv("sample.csv") 

#As sample.csv file got headers, we can sort the obtained data frame by Name, age and height
#Since headers are available, we can take the header name as per our requirement
# axis can be either 0 or 1, here 0 means 'index' and '1' means 'column
# ascending can be either True/False and if True, it gets arranged in ascending order ,
#if False, it gets arranged in descending order
#inplace = true/fase
#Output returned will be a sorted data frame
csvData.sort_values(["Name", "Age", "Height"], axis=0, 
				ascending=[True,True,True], 
inplace=True) 

#displaying sorted data frame
print(csvData )
