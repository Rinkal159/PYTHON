import pandas as pd

#* PANDAS 

data = {
    "names" : ["Rinkal", "Krina", "Mahi", "devang", "rudra", "kaushal"],
    "age" : [18, 23, 19, 20, 13, 25]
}

#series : 1-D labeled array
series1 = pd.Series([1,2,3,4,5])
print(series1) 
print(series1[0]) 

#series with custom index
series2 = pd.Series([1,2,3,4,5], index=['a', 'b', 'c', 'd', 'e'])
print(series2['c'])

# datafram : 2-D labled array (row + column)
data_frame = pd.DataFrame(data)
print(data_frame) #print all data
print(data_frame.head()) #print first five data
print(data_frame.tail()) #print last five data
print(data_frame["age"]) #accessing one column