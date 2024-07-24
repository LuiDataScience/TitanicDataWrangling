# Titanic Data Wrangling Project

<<<<<<< HEAD
## Overview
This project involves cleaning and preparing the Titanic dataset for analysis and visualization. The dataset is sourced from [Kaggle's Titanic - Machine Learning from Disaster competition](https://www.kaggle.com/c/titanic).

=======
>>>>>>> 2b4c528fa7e98f9bce0848f03fc11b2b9a378049
## Objective
A comprehensive project focused on cleaning and preparing the Titanic dataset, making it ready for data analysis and visualization.

## Steps
<<<<<<< HEAD

### 1. Set Up the Environment
- Ensure Python and required libraries (pandas, matplotlib, seaborn, scikit-learn) are installed.
- Set up a project directory and include the Titanic dataset (`train.csv`).

### 2. Data Cleaning
- Create a file named `data_cleaning.py` and use the following code:
=======
1. **Set Up the Environment**
   - Ensure Python and required libraries (pandas) are installed.
   - Set up a project directory and include the Titanic dataset (`train.csv`).

2. **Create a Data Cleaning Script**
   - Create a file named `data_cleaning.py` and use the following code:
>>>>>>> 2b4c528fa7e98f9bce0848f03fc11b2b9a378049

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
<<<<<<< HEAD

=======
# TitanicDataWrangling
A comprehensive project focused on cleaning and preparing the Titanic dataset, making it ready for data analysis and visualization.

## Exploratory Data Analysis (EDA) Project

### Objective
The objective of this project is to perform exploratory data analysis (EDA) on the Titanic dataset to uncover data trends and relationships.

### Steps
1. **Set Up the Environment**
   - Ensure Python and the required libraries (pandas, matplotlib, seaborn) are installed.
   - Set up a project directory and include the cleaned dataset (`cleaned_train.csv`).

2. **EDA Script**
   - Create a file named `eda.py` and use the following code:

     ```python
     import pandas as pd
     import matplotlib.pyplot as plt
     import seaborn as sns

     # Load the cleaned dataset
     df = pd.read_csv('cleaned_train.csv')

     # Visualize the distribution of ages
     plt.figure(figsize=(10, 6))
     sns.histplot(df['Age'], bins=30, kde=True)
     plt.title('Age Distribution')
     plt.xlabel('Age')
     plt.ylabel('Frequency')
     plt.show()

     # Visualize the survival rate by passenger class
     plt.figure(figsize=(10, 6))
     sns.barplot(x='Pclass', y='Survived', data=df)
     plt.title('Survival Rate by Passenger Class')
     plt.xlabel('Passenger Class')
     plt.ylabel('Survival Rate')
     plt.show()
     ```

### Results
#### Data Visualization
The exploratory data analysis revealed the following trends and relationships in the data:

1. **Age Distribution**
   - The age distribution was visualized to understand the age range of passengers.
   - Key insight: The majority of passengers are concentrated in the younger age range.

   ![Age Distribution](images/age_distribution.png)

2. **Survival Rate by Passenger Class**
   - The relationship between passenger class and survival rate was visualized to analyze survival rates across classes.
   - Key insight: Passengers in the 1st class have the highest survival rate.

   ![Survival Rate by Passenger Class](images/survival_rate_by_class.png)

### Next Steps
1. **Model Building**
   - Create a file named `ml_model.py` to build and evaluate machine learning models using the cleaned dataset.

### Conclusion
This project successfully performed exploratory data analysis on the Titanic dataset, uncovering key trends and relationships. The insights gained from this analysis prepare us for the next step of building machine learning models.
>>>>>>> 2b4c528fa7e98f9bce0848f03fc11b2b9a378049
