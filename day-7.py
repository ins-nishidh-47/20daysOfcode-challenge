import pandas as pd
import matplotlib.pyplot as plt

# Sample Data Creation
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, None, 28],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai'],
    'Salary': [50000, 60000, 55000, 70000, 45000]
})

# Display Basic Information
print("Initial Data:\n", data)
print("\nData Info:\n")
print(data.info())
print("\nStatistics:\n", data.describe())

# Handling Missing Values
data['Age'].fillna(data['Age'].mean(), inplace=True)

# Removing Duplicates
data.drop_duplicates(inplace=True)

# Sorting Data
data.sort_values(by='Salary', ascending=False, inplace=True)
print("\nSorted Data by Salary:\n", data)

# Indexing and Selection
print("\n.loc Example:\n", data.loc[0, 'Name'])
print("\n.iloc Example:\n", data.iloc[1, 2])
print("\nPeople Above Age 30:\n", data[data['Age'] > 30])

# Data Transformation
data['Salary'] = data['Salary'].apply(lambda x: x * 1.1)  # 10% hike
print("\nData After Salary Increment:\n", data)

# Grouping
city_avg_salary = data.groupby('City')['Salary'].mean()
print("\nAverage Salary by City:\n", city_avg_salary)

# Data Merging
data2 = pd.DataFrame({
    'City': ['Delhi', 'Mumbai', 'Chennai'],
    'Population': [18000000, 20000000, 10000000]
})
merged_data = pd.merge(data, data2, on='City')
print("\nMerged Data:\n", merged_data)

# Data Visualization
plt.figure(figsize=(6, 4))
merged_data.plot(x='City', y='Salary', kind='bar', title='Average Salary by City')
plt.show()

# Pivot Table Example
pivot_table = data.pivot_table(values='Salary', index='City', aggfunc='mean')
print("\nPivot Table - Average Salary by City:\n", pivot_table)

# Date and Time Handling
data['Joining_Date'] = pd.to_datetime(['2023-01-01', '2021-05-15', '2022-03-10', '2020-07-21', '2024-02-28'])
print("\nData with Joining Date:\n", data)

# MultiIndex Example
data.set_index(['City', 'Name'], inplace=True)
print("\nMultiIndex Data:\n", data)

# Adding a Calculated Column
data['Annual_Salary'] = data['Salary'] * 12
print("\nData with Annual Salary:\n", data)

# File Handling
data.to_csv('final_data.csv', index=False)
print("\nData saved to 'final_data.csv'")
