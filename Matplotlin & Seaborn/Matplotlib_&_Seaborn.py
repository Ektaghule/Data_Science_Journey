import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_customers = pd.read_excel('customers.xlsx')
data_purchases =  pd.read_excel('purchases.xlsx')
data_products = pd.read_excel('products.xlsx')

data_customers.isnull().sum()
print(data_customers.head())

data_purchases.isnull().sum()
print(data_purchases.columns)
data_purchases['paid'] = (
    data_purchases['paid']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)
print(data_purchases['paid'].dtype)
data_purchases.drop(columns=['Unnamed: 0'], inplace=True)
print(data_purchases.head())

data_products.isnull().sum()
data_products.drop(columns=['Unnamed: 0'], inplace=True)
print(data_products.head())

data_customers['id'] = data_customers['id'].astype(object) 
data_purchases['id'] = data_purchases['id'].astype(object) 
data_products['id'] = data_products['id'].astype(object) 
data_customers['postcode'] = data_customers['postcode'].astype(object)

print(data_products.columns)
print(data_products['cost'].dtype)
data_products['cost'] = (
    data_products['cost']
    .str.replace('$', '', regex=False)
    .astype(float)
)

avg_cost_per_company = data_products.groupby('company')['cost'].mean().reset_index()
print(avg_cost_per_company)

#Create a bar plot where in x-axis we have company and in y-axis we have cost per campany
plt.figure(figsize=(10,5))
plt.bar(avg_cost_per_company['company'], avg_cost_per_company['cost'], color = 'pink')
plt.title('Average cost per company', fontsize = 16)
plt.xlabel('Compnay', fontsize=12)
plt.ylabel('Avg Cost', fontsize=12)
plt.xticks(rotation=70)
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()
plt.savefig('Bar.png')

#Bar plot is used to represent the categorical data
#Box plot is used to detect the outliers

plt.boxplot(data_products['cost'])
plt.title("Box plot of the products cost", fontsize=16)
plt.ylabel('Cost of the product')
plt.show()

plt.boxplot(data_purchases['paid'])
plt.title("Box plot of paid from purchases")
plt.ylabel('paid customers of the product')
plt.show()

#Gender distribution: Pie chart
gender_count = data_customers['gender'].value_counts()
print(gender_count)
plt.pie(gender_count, autopct='%1.1f%%', labels=gender_count.index)
plt.title('Gender Distribution of customers')
plt.show()

#Visualize the customer spending patterns over time on a month basis using a line plot 
data_purchases['purch_date'] = pd.to_datetime(data_purchases['purch_date'])
data_purchases['month'] = data_purchases['purch_date'].dt.month
monthly_amount = data_purchases.groupby('month')['amount'].sum()

plt.plot(monthly_amount.index, monthly_amount.values, marker = 'o')
plt.title('Total Customer Spending Over Time (Monthly)')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.grid(True)
plt.show()

#Seaborn is simply build on top of Matplotlib
tips = sns.load_dataset('tips')
print(tips)

sns.barplot(x='day',y='tip',data=tips, estimator=sum)
plt.title('Total tips by day')
plt.xlabel('Day')
plt.ylabel('Total Tips')
plt.show()

#KDE Plot: Visualise the probality density funtion of any given variable.
sns.kdeplot(data=tips,x='total_bill', hue='time', fill=True)
plt.title('KDE plot of the total bill')
plt.xlabel('Total Bill')
plt.show()

#Boxplot
sns.boxplot(x='day', y='tip',data=tips)
plt.title('Distribution of tips per day')
plt.xlabel('Day')
plt.ylabel('Tips')
plt.show()

#Explore about the voilin plot which is used to detect the outliersa just like the boxplot.
sns.violinplot(x='day',y='tip',data=tips)
plt.title('Distribution of tips per day in voilin plot')
plt.xlabel('Day')
plt.ylabel('Tips')
plt.show()

#Pairplot: when you don't want to check the plots one by one, you want to see the pairing in one go then pairplot will give all the permutations and combination in one go.
sns.pairplot(data=tips) 
plt.show()

#Regrassion plot: For plotion the Linear regression of the ML
sns.regplot(x='total_bill', y='tip', data=tips)
plt.show()

#Sctter Plot:
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.show()

#Categorical Plot:
sns.catplot(x='smoker',y='tip', data=tips)
plt.show()

#Correlation coefficient: A factor which determine the value between -1 to +1. It is one of the feature selection technique.
numeric_tips = tips.select_dtypes(include='number')
correlation_coefficient = numeric_tips.corr()
print(correlation_coefficient)

sns.heatmap(correlation_coefficient, annot=True)
plt.title('Correlation Coefficient Matrix')
plt.show()

