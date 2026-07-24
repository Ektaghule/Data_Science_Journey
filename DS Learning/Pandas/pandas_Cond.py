import pandas as pd
import numpy as np

data = pd.read_csv("Titanic-Dataset.csv")
print(data.head())

print(data.info()) #Display the information about the dataset, including the number of non-null entries and data types for each column.

data['Country'] = 'USA' # Add a new column 'Country' with the value 'USA' for all rows
print(data.head()) # Display the first few rows of the updated dataset with the new 'Country' column.

#To place the country column after the 'Name' column, we can use the following code:
data.insert(4, 'Country', data.pop('Country')) # Move the 'Country' column to the desired position (after 'Name'), insert method (index no, column name, column data) and pop method (to remove the column from its original position).
print(data.head()) # Display the first few rows of the updated dataset with the 'Country' column.

#Concatenate the 'Name' and 'Country' columns into a new column called 'Name_Country'
data['Name_Country'] = data['Name'] + ' - ' + data['Country'] # Concatenate the 'Name' and 'Country' columns with a separator ' - '
print(data.head()) # Display the first few rows of the updated dataset with the new 'Name_Country' column.

# .loc and .iloc are two different methods in pandas used for selecting data from a DataFrame, but they have some key differences:
# .loc is label-based, meaning it selects rows and columns by their labels (names).
# .iloc is integer position-based, meaning it selects rows and columns by their integer index positions.
dataframe = data.loc[0:5, ['Name', 'Country']] # Select rows 0 to 5 and columns 'Name' and 'Country' using .loc
print(dataframe) # Display the selected rows and columns using .loc

dataframe = data.iloc[0:5, [3, 4]] # Select rows 0 to 5 and columns at index positions 3 and 4 using .iloc
print(dataframe) # Display the selected rows and columns using .iloc

#Acess details of id's from 500 to 505 
print(data.loc[500:505, ['Name', 'Country']]) # Select rows 500 to 505 and columns 'Name' and 'Country' using .loc

data = data.drop(columns=['Name_Country']) # Drop the 'Name_Country' column from the dataset
print(data.head()) # Display the first few rows of the updated dataset after dropping the 'Name_Country' column.

data = data.rename(index={0: 'first', 1: 'second', 2: 'third', 3: 'fourth', 4: 'fifth'}) # Rename the index of the DataFrame using the custom index
print(data.head()) # Display the first few rows of the updated dataset with the new index.

selected_data = data.loc[['first', 'second'], ['Name', 'Country']] # Select rows with custom index and columns 'Name' and 'Country' using .loc
print(selected_data) # Display the selected rows and columns using .loc with custom index.

unique_genders = data['Sex'].unique() # Get the unique values in the 'Sex' column
print("Unique genders in the dataset:", unique_genders) # Display the unique values in the 'Sex' column.

count_unique_genders = data['Sex'].nunique() # Get the count of unique values in the 'Sex' column
print("Count of unique genders in the dataset:", count_unique_genders) # Display the count of unique values in the 'Sex' column.

gender_counts = data['Sex'].value_counts() # Get the count of each unique value in the 'Sex' column
print("Count of each unique gender in the dataset:\n", gender_counts) # Display the count of each unique value in the 'Sex' column.

renamed_data = data.rename(columns={'Sex': 'Gender', 'Pclass': 'PassengerClass'}) # Rename the 'Sex' column to 'Gender' and 'Pclass' column to 'PassengerClass'
print(renamed_data.head()) # Display the first few rows of the updated dataset with the renamed columns.

data_purchases = pd.read_excel('purchases.xlsx') # Read the purchases data from an Excel file into a DataFrame
print(data_purchases.head()) # Display the first few rows of the purchases DataFrame

data_purchases = data_purchases.drop(columns =["Unnamed: 0"]) # Drop the 'Unnamed: 0' column from the purchases DataFrame
print(data_purchases.head()) # Display the first few rows of the updated purchases DataFrame after dropping the 'Unnamed: 0' column.

data_purchases ['purch_date'] = pd.to_datetime(data_purchases['purch_date']) # Convert the 'Date' column in the purchases DataFrame to datetime format
print(data_purchases.head()) #Display the first few rows of the updated purchases DataFrame after converting the 'Date' column to datetime format.

data_purchases['id'] = data_purchases['id'].astype(str) # Convert the 'id' column in the purchases DataFrame to string format
print(data_purchases.head()) # Display the first few rows of the updated purchases DataFrame after converting the 'id' column to string format.

data_purchases['paid'] = data_purchases['paid'].str.replace('[$,]', '', regex=True).astype(float) # Remove the dollar sign and commas from the 'paid' column in the purchases DataFrame and convert it to float format
print(data_purchases.head()) # Display the first few rows of the updated purchases DataFrame after cleaning the 'paid' column and converting it to float format.

data_products = pd.read_excel('products.xlsx') # Read the products data from an Excel file into a DataFrame
print(data_products.head()) # Display the first few rows of the products DataFrame

data_products = data_products.drop(columns =["Unnamed: 0"]) # Drop the 'Unnamed: 0' column from the products DataFrame
print(data_products.head()) # Display the first few rows of the updated products DataFrame after dropping the 'Unnamed: 0' column.

data_products['id'] = data_products['id'].astype(object) # Convert the 'id' column in the products DataFrame to object format
print(data_products.head()) # Display the first few rows of the updated products DataFrame after converting the 'id' column to object format.

data_products['cost'] = data_products['cost'].str.replace('[$,]', '', regex=True).astype(float) # Remove the dollar sign and commas from the 'cost' column in the products DataFrame and convert it to float format
print(data_products.dtypes) # Display the first few rows of the updated products DataFrame after cleaning the 'cost' column and converting it to float format.

#Concat is used to manipulate and combine multiple dataframes in pandas.
combined_data = pd.concat([data_purchases, data_products,data], axis=0) # Concatenate the purchases, products, and Titanic datasets along the rows (axis=0) to create a combined DataFrame and axix=1 means to concatenate along the columns.
print(combined_data.head()) # Display the first few rows of the combined DataFrame after concatenation.

data_customers = pd.read_excel('customers.xlsx') # Read the customers data from an Excel file into a DataFrame
print(data_customers.head()) # Display the first few rows of the customers DataFrame

#Merge is used to combine two dataframes based on a common column or index.
merged_data = pd.merge(data_customers, data_products, on='id', how='inner') # Merge the customers and products DataFrames based on the 'id' column using an inner join
print(merged_data.head()) # Display the first few rows of the merged DataFrame after merging the customers and products DataFrames.

data1_customers = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'product':['book', 'pen', 'pencil']
})

data2_purchases = pd.DataFrame({
    'id': [1, 2, 4],
    'product':['book', 'pen', 'pencil'],
    'paid': [10.0, 20.0, 30.0]
})

data_merged = pd.merge(data1_customers, data2_purchases, on='id', how='inner', suffixes=('_customer', '_purchase')) # Merge the two DataFrames based on the 'id' column using an inner join and add suffixes to distinguish between columns with the same name
print(data_merged) # Display the merged DataFrame after merging the two DataFrames with suffixes to distinguish between columns with the same name.

#Difference between concat, merge, and join in pandas:
#1. Concat: Concatenation is used to combine two or more DataFrames along a particular axis (rows or columns). It does not require a common column or index. It simply stacks the DataFrames together.
data1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
data2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
concatenated_data = pd.concat([data1, data2], axis=0) # Concatenate the two DataFrames along the rows (axis=0) to create a new DataFrame
print(concatenated_data) # Display the concatenated DataFrame after combining the two DataFrames along the rows.

#2. Merge: Merging is used to combine two DataFrames based on a common column or index. It allows for more complex operations, such as inner, outer, left, and right joins, similar to SQL joins.
data1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
data2 = pd.DataFrame({'id': [1, 2, 4], 'paid': [10.0, 20.0, 30.0]})
merged_data = pd.merge(data1, data2, on='id', how='inner') # Merge the two DataFrames based on the 'id' column using an inner join to create a new DataFrame
print(merged_data) # Display the merged DataFrame after combining the two DataFrames based on the common 'id' column using an inner join.

#3. Join: Joining is a method that is used to combine two DataFrames based on their index or a common column. It is similar to merging but is more convenient when working with DataFrames that have the same index or when you want to join on the index.
data1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
data2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]}, index=['a', 'b', 'd'])
joined_data = data1.join(data2, how='inner') # Join the two DataFrames based on their index using an inner join to create a new DataFrame
print(joined_data) # Display the joined DataFrame after combining the two DataFrames based on their index using an inner join.

#Missing values
data.isnull().sum() # Check for missing values in the dataset and display the count of missing values for each column
print(data.isnull().sum()) # Display the count of missing values for each column in the dataset

#Missing values can be handled in several ways, including dropping rows or columns with missing values, filling missing values with a specific value, or using interpolation methods to estimate missing values. Here are some examples:
#1. Dropping rows with missing values 
customers_copy = data.copy() # Create a copy of the original dataset to avoid modifying it directly
customers_copy = customers_copy.dropna() # Drop rows with any missing values from the dataset
print(customers_copy.head()) # Display the first few rows of the updated dataset after dropping rows with missing values
#dropna() method is used only when you have a small number of missing values and you don't want to lose too much data. Otherwise, avoid dropping rows with missing values, as it can lead to loss of valuable information.

#2. Data imputation: Filling missing values with a specific value, such as the mean, median, or mode of the column. This is useful when you want to retain all rows in the dataset and avoid losing information.
#Fill missing values in the 'Age' column with the mean age
mode_sex = data['Sex'].mode()[0] # Calculate the mode of the 'Sex' column to fill missing values
print("Mode of 'Sex' column:", mode_sex) # Display the mode of the 'Sex' column

data_sex = data.copy() # Create a copy of the original dataset to avoid modifying it directly
data_sex.fillna({'Sex': mode_sex}, inplace=True) # Fill missing values in the 'Sex' column with the mode value
print(data_sex.head()) # Display the first few rows of the updated dataset after filling missing values in the 'Sex'

#ffill() method is used to fill missing values with the previous value in the column. This is useful when you have a time series dataset and you want to fill missing values with the last known value.
data_ffill = data.copy() # Create a copy of the original dataset to avoid modifying it
data_ffill.ffill(inplace=True)
print(data_ffill.head()) # Display the first few rows of the updated dataset after filling missing values using forward fill method

#bfill() method is used to fill missing values with the next value in the column. This is useful when you have a time series dataset and you want to fill missing values with the next known value.
data_bfill = data.copy() # Create a copy of the original dataset to avoid modifying it
data_bfill.bfill(inplace=True)
print(data_bfill.head()) # Display the first few rows of the updated dataset after filling missing values using backward fill method 

#mean() method is used to calculate the mean of a column. This is useful when you want to fill missing values with the average value of the column.
data_mean = data.copy() # Create a copy of the original dataset to avoid modifying it
data_mean['Age'] = data_mean['Age'].fillna(data_mean['Age'].mean())
print(data_mean.head()) # Display the first few rows of the updated dataset after filling missing values

#median() method is used to calculate the median of a column. This is useful when you want to fill missing values with the middle value of the column.
data_median = data.copy() 
data_median['Age'] = data_median['Age'].fillna(data_median['Age'].median())
print(data_median.head())

#Imputed the missing values with the 'Unknown'
data_customers['email'] = data_customers['email'].fillna('Unknown') # Fill missing values in the 'email' column with the string 'Unknown'
print(data_customers) # Display the first few rows of the updated customers DataFrame after filling missing values in the 'email' column with 'Unknown'

#Data Analysis: Aggregation
aggregate_purchase = data_purchases.groupby('customer_num').agg({'amount':'sum', 'paid':'sum'})
print(aggregate_purchase)

total_amount = data_purchases.groupby('purch_date').agg({'amount':'sum', 'paid':'sum'})
print(total_amount)