### Mid-Term Exam (15 marks)

You have been given access to an SQLite database (`survey.db3`) generated from the customer survey data.  The database contains two tables: `support` and `survey`. 

#### Data Schema for the `support` Table  

| Column Name     | Data Type  | Description  |
|----------------|-----------|---------------------------------------------------------|
| `id`           | Discrete  | The unique identifier of the support ticket. |
| `customer_id`  | Discrete  | The unique identifier of the customer. |
| `category`     | Nominal   | The category of the support request, can be one of **Feedback, Billing Enquiry, Bug, Installation Problem, Other**.  |
| `status`       | Nominal   | The current status of the support ticket, one of **Open, In Progress, or Resolved**. |
| `creation_date` | Discrete  | The date the ticket was created (any date in 2023). |
| `response_time` | Discrete  | The number of days taken to respond to the support ticket. |
| `resolution_time` | Continuous | The number of hours taken to resolve the support ticket, rounded to 2 decimal places. |

### Data Schema for the `survey` Table  

| Column Name   | Data Type | Description |
|--------------|----------|-------------|
| `id`         | Integer  | Unique identifier for each survey entry. |
| `customer_id` | Integer  | Unique identifier for the customer who completed the survey. |
| `rating`     | Integer  | Rating given by the customer (e.g., scale from 1-5). |
| `timestamp`  | String (Datetime) | The date and time when the survey was submitted. |
---
### Question 1: Extract (3 marks)

- Write a Python function, called `extract`  to retrieve all records from a specified table and return a `pandas` DataFrame.  
  - Use the `pd.read_sql()` function to fetch the data.  
  - Ensure the function returns a `pandas` DataFrame.  
- Extract data from both the **`support`** and **`survey`** tables.  
- Display the first five rows of the extracted data for each table.  
- Print the total number of records in both the **`support`** and **`survey`** tables.  
---
### Question 2: Transform (5 marks)  

- Perform **data cleaning** on the `support` table.  
- You can use the **COALESCE** function to replace missing values according to the specified criteria.  

#### **Data Cleaning Requirements**  

| Column Name       | Transformation Rule |
|------------------|---------------------------------------------------------|
| `customer_id`    | Replace missing values with **0**. |
| `category`       | Replace missing values with **"Other"**. |
| `status`         | Replace missing values with **"Resolved"**. |
| `creation_date`  | Replace missing values with **"2023-01-01"**. |
| `response_time`  | Replace missing values with **0**. |
---
### Question 3: Transform (5 marks)

- Use the cleaned data from Question 2 and calculate the minimum and maximum response time for each category of support ticket. 

- Your output should include the columns `category`, `min_response` and `max_response`. 

- Values should be rounded to two decimal places where appropriate. 
---
### Question 4: Load (2 marks)

- Save the data from Question 3 into a CSV file named `respond_time.csv`.
---