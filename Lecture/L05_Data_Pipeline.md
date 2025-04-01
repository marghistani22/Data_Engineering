# **Lecture 05: Data Pipeline**

This lecture explores Python Pandas Common Methods for Queries, data modelling, transformation and loading.
---

# Pandas Basics for Data Engineering Beginners

## 1. `read_csv()` – Load Data from a CSV File
📌 Used to import structured data into a **DataFrame**
```python
import pandas as pd

df = pd.read_csv("employees.csv")
print(df.head())  # Display the first 5 rows
```

---

## 2. `info()` – Get Dataset Overview
📌 Shows data types, missing values, and memory usage
```python
df.info()
```

---

## 3. `describe()` – Get Summary Statistics
📌 Provides mean, median, min, max, and percentiles for numerical columns
```python
df.describe()
```

---

## 4. `head()` and `tail()` – View Sample Rows
📌 `head(n)` → First `n` rows | `tail(n)` → Last `n` rows
```python
df.head(3)  # First 3 rows
df.tail(2)  # Last 2 rows
```

---

## 5. `isnull().sum()` – Check Missing Values
📌 Identifies missing data for **cleaning and preprocessing**
```python
df.isnull().sum()
```

---

## 6. `fillna()` – Fill Missing Values
📌 Replaces `NaN` values with a specified value (e.g., mean, median)
```python
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())  # Fill missing salary with average
```

---

## 7. `groupby()` – Aggregate Data
📌 Used to group data and apply functions like `sum()`, `count()`, `mean()`
```python
df.groupby("Department")["Salary"].mean()  # Average salary per department
```

---

## 8. `sort_values()` – Sort Data
📌 Sorts by a specific column (ascending or descending)
```python
df.sort_values(by="Salary", ascending=False)  # Sort salaries in descending order
```

---

## 9. `apply()` – Apply Custom Functions
📌 Used to apply a function to each row or column
```python
df["Updated_Salary"] = df["Salary"].apply(lambda x: x * 1.1)  # Increase salary by 10%
```

---

## 10. `merge()` – Join DataFrames
📌 Works like SQL JOINs (`inner`, `left`, `right`, `outer`)
```python
df1 = pd.DataFrame({"EmpID": [101, 102], "Name": ["Alice", "Bob"]})
df2 = pd.DataFrame({"EmpID": [101, 103], "Salary": [60000, 70000]})

merged_df = pd.merge(df1, df2, on="EmpID", how="inner")
print(merged_df)
```

---

## 11. `to_csv()` – Export Data
📌 Save processed data back to a CSV file
```python
df.to_csv("cleaned_data.csv", index=False)
```
---

### **Resources for Lecture 05**

#### 📑 **Lecture Slides**
- [Access the slides on Canva](https://www.canva.com/design/DAGiG623q9g/ma31lpJiiKJvcnJW2vE4uA/view?utm_content=DAGiG623q9g&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h090ed2e976)

#### 📂 **Further Reading**
- [Data Piplelines Pocket Reference](https://www.amazon.com/Data-Pipelines-Pocket-Reference-Processing/dp/1492087831)
- [TextBook](https://www.amazon.com/Fundamentals-Data-Engineering-Robust-Systems/dp/1098108302)