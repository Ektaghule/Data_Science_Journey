import numpy as np
#Pandas is a module that is specifically used to manipulate the data (basically analyse the data). It is simple and intuitive ro do any specific data operation. Also it can handle a variety of data formats and sources.
import pandas as pd

data = pd.read_csv(r'D:\Study\DS\Python Learning\Titanic-Dataset.csv')
print(data.head()) #Displays the first 5 rows of the dataset

type= data.dtypes #Displays the data type of each column in the dataset
print(type)

print(data.tail()) #Displays the last 5 rows of the dataset

#Pandas has 2 types of data structures: Series and DataFrame. Series is a one-dimensional array that can hold any data type. DataFrame is a two-dimensional array that can hold multiple data types.
#Series is a one-dimensional array-like structure that can hold a sequence of value of any data type. Each value in a Series is associated with an index, which is used to access the values in the Series. The index can be either a default integer index or a custom index.

#Let's create a Series from scalar value with the custom index.
series_scalar = pd.Series(5, index=['a', 'b', 'c', 'd', 'e'])
print(series_scalar)
print(series_scalar['e']) #Displays the value associated with the index 'e'.

data = [10, 20, 30, 40, 50] #Creating a Series from a list of values. The index will be the default integer index.
series_list = pd.Series(data)
print(series_list)

data_array = np.array([1, 2, 3, 4, 5]) #Creating a Series from a numpy array. The index will be the default integer index.
series_array = pd.Series(data_array)
print(series_array)

data_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} #Creating a Series from a dictionary. The index will be the keys of the dictionary.
series_dict = pd.Series(data_dict)
print(series_dict)
print(series_dict[0:3]) #Displays the first 3 values of the Series. The index will be the default integer index.

#Attributes of Series:
#1. index: Returns the index of the Series.
#2. values: Returns the values of the Series.
data1 = ['Pune','Washington','New York','London','Paris']
index1 = ['India','USA','USA','UK','France']
series = pd.Series(data1, index=index1)
print(series) 
print("Index of the Series:",series.index) #Displays the index of the Series.
print("Values of the Series:",series.values) #Displays the values of the Series.
print("Data type of the Series:",series.dtype) #Displays the data type of the Series.
print("Shape of the Series:",series.shape) #Displays the number of rows and columns in the Series. Since Series is a one-dimensional array, it will return the number of rows only.
print("Size of the Series:",series.size) #Displays the number of elements in the Series.
print("Memory usage of the Series:",series.memory_usage()) #Displays the memory usage of the Series in bytes.
print("Is the Series empty?:",series.empty) #Returns True if the Series is empty, otherwise returns False.
print("Is this Series contain NaN values?:",series.hasnans) #Returns True if the Series contains NaN(Not a Number) values, otherwise returns False.
print("Is the Series unique?:",series.is_unique) #Returns True if the Series contains unique values, otherwise returns False.
print("Dimension of the Series:",series.ndim) #Returns the number of dimensions of the Series. Since Series is a one-dimensional array, it will return 1.

#Methods of Series:
#1. head(): Returns the first n rows of the Series. The default value of n is 5. If n is greater than the number of rows in the Series, it will return all the rows.
#2. tail(): Returns the last n rows of the Series. The default value of n is 5. If n is greater than the number of rows in the Series, it will return all the rows.

#3.describe(): Returns the summary statistics of the Series. It includes count, mean, standard deviation, minimum, maximum and quartiles.
print("Describe of the Series:",series.describe()) #Displays the summary statistics of the Series.

#4. value_counts(): Returns the count of unique values in the Series. It returns a Series with the unique values as index and their counts as values.
data2 = ['Pune','Washington','New York','London','Paris','Pune','Washington','New York','London','Paris']
series2 = pd.Series(data2)
print("Value counts of the Series:",series2.value_counts()) #Displays the count of unique values in the Series.

#5. sort_values(): Returns a Series sorted by the values. It returns a new Series with the same index as the original Series.
print("Series sorted by values:",series2.sort_values()) #Displays the Series sorted by the values. The default sorting order is ascending. To sort in descending order, we can use the parameter ascending=False.

#6. drop(): Returns a Series with the specified index removed. It returns a new Series with the same values as the original Series.
print(series2.drop(0)) #Displays the Series with the index 0 removed. The default value of inplace is False. If inplace is True, it will modify the original Series and return None.
print(series2.drop(0, inplace=True)) #Displays the Series with the index 0 removed. The default value of inplace is False. If inplace is True, it will modify the original Series and return None.

#7. isnull(): Returns a Series with True for NaN values and False for non-NaN values. It returns a new Series with the same index as the original Series.
data3 = [1, 2, 3, 4, 5, np.nan, 7, 8, 9, 10]
series3 = pd.Series(data3)
print("Is the Series contain NaN values?:",series3.isnull()) #Displays a Series with True for NaN values and False for non-NaN values.

#Task: Add,Subtract,Multiply and Divide two Series.
S1 = pd.Series([1, 2, 3, 4, 5])
S2 = pd.Series([10, 20, 30, 40, 50])
print("Addition of two Series:",S1+S2) #Displays the addition of two Series. It returns a new Series with the same index as the original Series.
print("Subtraction of two Series:",S1-S2) #Displays the subtraction of two Series. It returns a new Series with the same index as the original Series.
print("Multiplication of two Series:",S1*S2) #Displays the multiplication of two Series. It returns a new Series with the same index as the original Series.
print("Division of two Series:",S1/S2) #Displays the division of two Series. It returns a new Series with the same index as the original Series.

#Task: Stimulate the same approach with DataFrame. And cover all the attributes and methods of DataFrame.
data = {'Name': ['John', 'Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40, 45]}
df = pd.DataFrame(data)
print(df) #Displays the DataFrame.
print("Index of the DataFrame:",df.index) #Displays the index of the DataFrame.
print("Columns of the DataFrame:",df.columns) #Displays the columns of the DataFrame.
print("Values of the DataFrame:",df.values) #Displays the values of the DataFrame.
print("Data type of the DataFrame:",df.dtypes) #Displays the data type of the DataFrame.
print("Shape of the DataFrame:",df.shape) #Displays the number of rows and columns in the DataFrame.
print("Size of the DataFrame:",df.size) #Displays the number of elements in the DataFrame.
print("Memory usage of the DataFrame:",df.memory_usage()) #Displays the memory usage of the DataFrame in bytes.
print("Is the DataFrame empty?:",df.empty) #Returns True if the DataFrame is empty, otherwise returns False.
print("Is this DataFrame contain NaN values?:",df.isnull().values.any()) #Returns True if the DataFrame contains NaN(Not a Number) values, otherwise returns False.
print("Is the DataFrame unique?:",df.duplicated().any()) #Returns True if the DataFrame contains duplicate values, otherwise returns False.
print("Dimension of the DataFrame:",df.ndim) #Returns the number of dimensions of the DataFrame. Since DataFrame is a two-dimensional array, it will return 2.
print("Describe of the DataFrame:",df.describe()) #Displays the summary statistics of the DataFrame. It includes count, mean, standard deviation, minimum, maximum and quartiles.
print("Value counts of the DataFrame:",df['Age'].value_counts()) #Displays the count of unique values in the 'Age' column of the DataFrame.
print("DataFrame sorted by values:",df.sort_values(by='Age')) #Displays the DataFrame sorted by the 'Age' column. The default sorting order is ascending. To sort in descending order, we can use the parameter ascending=False.
print("Drop a column from the DataFrame:",df.drop('Age', axis=1)) #Displays the DataFrame with the 'Age' column removed. The default value of inplace is False. If inplace is True, it will modify the original DataFrame and return None.
print("Is null values in the DataFrame:",df.isnull()) #Displays a DataFrame with True for NaN values and False for non-NaN values. It returns a new DataFrame with the same index and columns as the original DataFrame.