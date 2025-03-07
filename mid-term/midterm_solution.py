#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import sqlite3


# In[ ]:


### Question 1: Extract (4 marks)

def extract(db_path, table_name):
    query = f"SELECT * From {table_name};"


    df = pd.read_sql_query(query, f"sqlite:///{db_path}")
    
    return df

# Extract data
db_path = "survey.db3"
df_support = extract(db_path, "support")
df_survey = extract(db_path, "survey")

print(f"Support Table: {df_support.shape[0]} records")
print(f"Survey Table: {df_survey.shape[0]} records")


# In[ ]:


### Question 2: Transform (5 marks)  

def transform(raw_data):
    clean_data = raw_data.copy()
    clean_data['customer_id'] = clean_data['customer_id'].astype(int)
    clean_data['customer_id'] = clean_data['customer_id'].fillna(0)

    category_list = ['Feedback', 'Billing Enquiry', 'Bug', 'Installation Problem', 'Other']
    clean_data['category'] = clean_data['category'].apply(lambda cat: cat if cat in category_list else 'Other')
    clean_data['category'] = clean_data['category'].astype("category")

    status_list = ['Open', 'In Progress', 'Resolved']
    clean_data['status'] = clean_data['status'].apply(lambda cat: cat if cat in status_list else 'Resolved')
    clean_data['status'] = clean_data['status'].astype("category")

    clean_data['response_time'] = clean_data['response_time'].astype(int)
    clean_data['response_time'] = clean_data['response_time'].fillna(0)

    return clean_data

df_cleaned = transform(df_support)
df_cleaned.head()


# In[ ]:


### Question 3: Transform and Load (5 marks)  

def aggregate_response_time(df: pd.DataFrame):
    df_grouped = df.groupby("category", observed = False)['response_time'].agg(['min', 'max']).reset_index()
    df_grouped.columns = ['category', 'min_response', 'max_response']
    df_grouped = df_grouped.round(2)
    return df_grouped

df_aggregated = aggregate_response_time(df_cleaned)
df_aggregated.head()


# In[ ]:


### Question 4: Load (1 marks)
def save_to_csv(df: pd.DataFrame, filename: str = "respond_time.csv"):
    df.to_csv(filename, index=False)

save_to_csv(df_aggregated)
print("Aggregated response time saved to respond_time.csv")

