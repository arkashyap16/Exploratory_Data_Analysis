# 🚢 Titanic Dataset - Exploratory Data Analysis (EDA)

This repository contains my submission for **Task 2** of the **AI & ML Internship Program**. The task focuses on performing **Exploratory Data Analysis (EDA)** on the Titanic dataset to understand its structure, relationships, and key patterns using statistical and visual techniques.

---

## 📌 Task Objective

> **Perform EDA** to gain insights about the data using **summary statistics** and **visualizations** with tools like Pandas, Matplotlib, Seaborn, and Plotly.

---

## 📂 Dataset

- **Name**: Titanic Dataset  
- **Source**: [Kaggle - Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- **File Used**: `Titanic-Dataset.csv`

---

## 🔧 Tools & Libraries Used

- Python 🐍
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Plotly

---

## 🧪 Data Cleaning

- Filled missing `Age` values with median
- Filled missing `Embarked` values with mode
- Dropped `Cabin` column due to excessive missing values

---

## 📊 EDA Highlights

### ✅ Summary Statistics
- Used `.describe()`, `.info()`, and `.isnull().sum()` to explore the data structure and missing values.

### 📉 Distribution Visualizations
- **Histogram**: Distribution of all numerical features
- **Boxplot**: `Age` distribution by `Pclass`
- **Countplot**: Survival counts and Gender vs Survival
- **Pie Chart**: Embarkment percentages
- **Heatmap**: Correlation matrix
- **Pairplot**: Relationships among `Age`, `Fare`, `Pclass`, and `Survived`

> (Note: Included screenshots of plots for better visualization on GitHub.)
![Screenshot 2025-06-26 194600](https://github.com/user-attachments/assets/fc3cf543-9287-4b21-9f82-32f6706529fb)
![Screenshot 2025-![Screenshot 2025-06-26 194718](https://github.com/user-attachments/assets/8b9d2f18-f1ce-4532-b499-6899df0a2a59)
06-26 194644](https://github.com/user-attachments/assets/0a21b867-2f35-43d6-b465-9078348f76de)
![Screenshot 2025-06-26 194630](https://github.com/user-attachments/assets/dba46bb1-091b-4e5b-95b3-1400668eb4f5)
![Screenshot 2025-06-26 194734](https://github.com/user-attachments/assets/ebbac773-ebc9-44e7-ae54-d3b5f8ee0418)
![Screenshot 2025-06-26 194747](https://github.com/user-attachments/assets/ccb08323-f4ed-4bc3-8a26-7e9ab31d3d1a)


