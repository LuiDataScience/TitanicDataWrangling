# Titanic Data Wrangling Project

## Objective
A comprehensive project focused on cleaning and preparing the Titanic dataset, making it ready for data analysis and visualization.

## Dataset Details
The Titanic dataset contains information about the passengers who were on board the Titanic when it sank on its maiden voyage. The dataset includes the following columns:

- **PassengerId**: Unique ID for each passenger
- **Survived**: Survival indicator (0 = No, 1 = Yes)
- **Pclass**: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
- **Name**: Name of the passenger
- **Sex**: Gender of the passenger
- **Age**: Age of the passenger
- **SibSp**: Number of siblings/spouses aboard the Titanic
- **Parch**: Number of parents/children aboard the Titanic
- **Ticket**: Ticket number
- **Fare**: Passenger fare
- **Cabin**: Cabin number
- **Embarked**: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

### Data Source
The dataset was obtained from Kaggle's Titanic competition. The dataset can be downloaded from the following link:
[Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data)

## Steps
1. **Set Up the Environment**
   - Ensure Python and required libraries (pandas) are installed.
   - Set up a project directory and include the Titanic dataset (`train.csv`).

2. **Data Cleaning**
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
