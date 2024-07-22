import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('cleaned_train.csv')

# Display the first few rows of the dataset
print("DataFrame Head:\n", df.head())

# Display the data types of each column
print("\nDataFrame Data Types:\n", df.dtypes)

# Ensure only numeric columns are selected for correlation matrix
numeric_df = df.select_dtypes(include=[float, int])

print("\nSelected Numeric Columns for Correlation Matrix:\n", numeric_df.head())

# Create a histogram of Age
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Create a bar chart of Survived
plt.figure(figsize=(10, 6))
sns.countplot(x='Survived', data=df)
plt.title('Survival Counts')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()

# Create a heatmap of the correlation matrix
plt.figure(figsize=(10, 6))
correlation_matrix = numeric_df.corr()
print("\nCorrelation Matrix:\n", correlation_matrix)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
