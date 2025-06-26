import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("Titanic-Dataset.csv")
df.head()
df.info()
df.describe()
df.isnull().sum()


df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

df.drop(columns=['Cabin'], inplace=True, errors='ignore')

df.select_dtypes(include='object').columns
print("Categorical columns:", df.select_dtypes(include='object').columns.tolist())

df.hist(figsize=(12, 10), color='skyblue', edgecolor='black')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(x='Pclass', y='Age', data=df)
plt.title('Age Distribution by Passenger Class')
plt.show()

sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.show()

sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival by Gender')
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only= True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare']], hue='Survived')
plt.show()

df['Embarked'].value_counts().plot.pie(autopct='%1.1f%%', shadow=True, figsize=(6,6))
plt.title('Passengers by Embarkment')
plt.ylabel('')
plt.show()

df.to_csv("Titanic-Dataset.csv", index=False)
