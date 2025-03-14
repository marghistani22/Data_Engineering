import pandas as pd
import sqlite3

db_path = 'survey.db3'
query = "SELECT * FROM support;"

support_df = pd.read_sql_query(query, f"sqlite:///{db_path}")
print(support_df.shape[0])

query = "SELECT * FROM survey;"
survey_df = pd.read_sql_query(query, f"sqlite:///{db_path}")
print(survey_df.shape[0])

cat_list = ['Feedback', 'Billing enquiry', 'Bug', 'Installation Problem', 'Other']
support_df['category'] = support_df['category'].fillna('Other')
support_df['category'] = support_df['category'].apply(lambda x: x if x in cat_list else 'Other')

status_list = ['Open', 'In Progress', 'Resolved']
support_df['status'] = support_df['status'].apply(lambda x: x if x in status_list else 'Resolved')

support_df['resolution_time'] = support_df['resolution_time'].str.strip().replace(r'(\d+)\s+hours', r'\1', regex=True)

support_df['response_time'] = support_df['response_time'].astype(int)
support_df['resolution_time'] = support_df['resolution_time'].astype(float)
print(support_df.dtypes)

db_path = 'survey.db3'
query = """ 
    SELECT 
        CASE 
            WHEN category IS NULL OR category = '-' THEN 'Other' 
            ELSE category
        END AS new_category,
        MIN(response_time) AS min_response, 
        MAX(response_time) AS max_response
    FROM support
    GROUP BY new_category;
    """

cat_df = pd.read_sql_query(query, f"sqlite:///{db_path}")
cat_df.columns = ['category', 'min_response', 'max_response']
print(cat_df)
cat_df.to_csv('respond_time.csv', index = False)