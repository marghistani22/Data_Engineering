import os
import pandas as pd
import sqlite3
import streamlit as st
from census import Census
from us import states

@st.cache_data
def extract_data():
    try:
        c = Census(os.environ.get('census_api_key'))  
        data_census = c.acs5.state_county_tract(
            fields=('NAME', 'C17002_001E', 'C17002_002E', 'C17002_003E', 'B01003_001E'),
            state_fips=states.MA.fips,  # Massachusetts
            county_fips="*", tract="*", year=2022
        )
        return pd.DataFrame(data_census)
    except Exception as e:
        st.error(f"Error fetching data from Census API: {e}")
        return pd.DataFrame()

def transform_data(df):
    try:
        df = df.rename(columns={
            'NAME': 'Location',
            'C17002_001E': 'Total Population',
            'C17002_002E': 'Below Poverty Level',
            'C17002_003E': 'Above Poverty Level',
            'B01003_001E': 'Total Census Population'
        })
        df['Poverty Rate'] = (df['Below Poverty Level'] / df['Total Population']) * 100
        return df[['Location', 'Total Population', 'Below Poverty Level', 'Above Poverty Level', 'Poverty Rate']]
    except Exception as e:
        st.error(f"Error transforming data: {e}")
        return df


def load_data(df):
    try:
        conn = sqlite3.connect("census_data.db")
        df.to_sql("census", conn, if_exists="replace", index=False)
        conn.close()
    except Exception as e:
        st.error(f"Error saving data to SQLite: {e}")


def dashboard():
    st.title("Census Data Dashboard")
    
    conn = sqlite3.connect("census_data.db")
    df = pd.read_sql("SELECT * FROM census", conn)
    conn.close()
    
    st.write("### Census Data Sample")
    st.dataframe(df.head())
    
    st.write("### Poverty Rate Distribution")
    st.bar_chart(df[['Location', 'Poverty Rate']].set_index('Location'))
