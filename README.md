# Titanic Data Wrangling Project

## Objective
A comprehensive project focused on cleaning and preparing the Titanic dataset, making it ready for data analysis and visualization.

## Steps
1. **Set Up the Environment**
   - Ensure Python and required libraries (pandas) are installed.
   - Set up a project directory and include the Titanic dataset (`train.csv`).

2. **Create a Data Cleaning Script**
   - Create a file named `data_cleaning.py` and use the following code:

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('train.csv')

# Display basic information about the dataset
print(df.info())

# Handle missing values (e.g., fill missing age with mean)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Detect and handle outliers (e.g., cap Fare values)
df = df[df['Fare'] < 300]

# Convert data types
df['Pclass'] = df['Pclass'].astype(int)
df['Survived'] = df['Survived'].astype(int)

# Remove duplicate data
df = df.drop_duplicates()

# Save the cleaned dataset
df.to_csv('cleaned_train.csv', index=False)

print("Data cleaning completed.")
# TitanicDataWrangling
A comprehensive project focused on cleaning and preparing the Titanic dataset, making it ready for data analysis and visualization.

