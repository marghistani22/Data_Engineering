### Mid-Term Exam (15 marks)

You have been given access to an SQLite database (`survey.db3`) generated from the customer survey data.  The database contains two tables: `support` and `survey`. 

#### Data Schema for the `support` Table  

| Column Name     | Data Type  | Description  |
|----------------|-----------|---------------------------------------------------------|
| `id`           | Discrete  | The unique identifier of the support ticket. |
| `customer_id`  | Discrete  | The unique identifier of the customer. |
| `category`     | Nominal   | The category of the support request, can be one of **Feedback, Billing Enquiry, Bug, Installation Problem, Other**.  |
| `status`       | Nominal   | The current status of the support ticket, one of **Open, In Progress, or Resolved**. |
| `creation_date` | Discrete  | The date the ticket was created. |
| `response_time` | Discrete  | The number of days taken to respond to the support ticket. |
| `resolution_time` | Continuous | The number of hours taken to resolve the support ticket, rounded to 2 decimal places.  |

### Data Schema for the `survey` Table  

| Column Name   | Data Type | Description |
|--------------|----------|-------------|
| `id`         | Integer  | Unique identifier for each survey entry. |
| `customer_id` | Integer  | Unique identifier for the customer who completed the survey. |
| `rating`     | Integer  | Rating given by the customer (e.g., scale from 1-5). |
| `timestamp`  | String (Datetime) | The date and time when the survey was submitted. |
---
### Question 1: Extract (4 marks)

- Complete `extract` function to retrieve all records from a specified table and return a `pandas` DataFrame.  
  - Use the `pd.read_sql()` function to fetch the data.  
  - Ensure the function returns a `pandas` DataFrame.  
- Extract data from both the **`support`** and **`survey`** tables.   
- Print the total number of records in both the **`support`** and **`survey`** tables.  
---
### Question 2: Transform (5 marks)  

- Perform **data cleaning** on the `support` table.  
- Make sure that the data type are correct as specified in the above table. 
- Replace missing values according to the specified criteria in the below table.
- You can use the SQLite **COALESCE** function or you can use any Python function.

#### **Data Cleaning Requirements**  

| Column Name       | Transformation Rule |
|------------------|---------------------------------------------------------|
| `customer_id`    | Replace missing/incorrect values with **0** if any. |
| `category`       | Replace missing/incorect  values with **"Other"** if any. |
| `status`         | Replace missing/incorrect values with **"Resolved"** if any. |
| `response_time`  | Replace missing/incorrect values with **0** if any.|
---
### Question 3: Transform (5 marks)

- Calculate the minimum and maximum response time for each category of support ticket. 
- Fix the missing/incorrect values as described in Question 2. 
- Your output should include the columns `category`, `min_response` and `max_response`. 
- Values should be rounded to two decimal places where appropriate. 
---
### Question 4: Load (1 marks)

- Save the data from Question 3 into a CSV file named `respond_time.csv`.
---