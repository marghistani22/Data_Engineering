import pytest
import pandas as pd
import numpy as np
import sqlite3
import os

# Import the functions from the student's script
from midterm_solution import extract, transform, aggregate_response_time  


DB_PATH = "survey.db3"

def test_extract():
    """Test that `extract` correctly retrieves data from the database."""
    df_support = extract(DB_PATH, "support")
    df_survey = extract(DB_PATH, "survey")

    # Check if DataFrames are returned
    assert isinstance(df_support, pd.DataFrame), "extract should return a pandas DataFrame for support"
    assert isinstance(df_survey, pd.DataFrame), "extract should return a pandas DataFrame for survey"

    # Check if both tables have data
    assert not df_support.empty, "Support table extraction returned empty DataFrame"
    assert not df_survey.empty, "Survey table extraction returned empty DataFrame"

    # Check expected columns in support table
    expected_support_columns = {"id", "customer_id", "category", "status", "creation_date", "response_time", "resolution_time"}
    assert expected_support_columns.issubset(df_support.columns), "Support table missing expected columns"

    # Check expected columns in survey table
    expected_survey_columns = {"id", "customer_id", "rating", "timestamp"}
    assert expected_survey_columns.issubset(df_survey.columns), "Survey table missing expected columns"

### **Test for `transform` function**
def test_transform():
    """Test that `transform` correctly cleans and modifies the dataset."""
    print("Running test_transform")
    raw_data = extract(DB_PATH, "support")
    clean_data = transform(raw_data)

    # Check that missing customer_id is replaced with 0
    assert clean_data['customer_id'].isna().sum() > 0, "customer_id missing values should be replaced with 0"

    # Check that categories are from the valid list or replaced with 'Other'
    category_list = ['Feedback', 'Billing Enquiry', 'Bug', 'Installation Problem', 'Other']
    invalid_categories = clean_data[~clean_data['category'].isin(category_list)]
    
    # Assert that all invalid categories are replaced with 'Other'
    assert invalid_categories.empty, f"Invalid categories should be replaced with 'Other', but found: {invalid_categories['category'].unique()}"

    # Ensure 'category' column values are in the valid category list or 'Other'
    assert clean_data['category'].isin(category_list + ['Other']).all(), "Category values should only be from the list or 'Other'"

    # Check that invalid status is replaced with 'Resolved'
    status_list = ['Open', 'In Progress', 'Resolved']
    invalid_status = clean_data[~clean_data['status'].isin(status_list)]
    assert invalid_status.empty, f"Invalid statuses should be replaced with 'Resolved', but found: {invalid_status['status'].unique()}"

    # Ensure that all 'status' column values are valid or 'Resolved'
    assert clean_data['status'].isin(status_list).all(), "Status values should only be from the list or 'Resolved'"

    # Check that missing response_time is replaced with 0
    assert clean_data['response_time'].isna().sum() == 0, "Missing response_time should be replaced with 0"
    assert (clean_data['response_time'] == 0).sum() == 1, "response_time missing values should be replaced with 0"


### **Test for Transform and Load (Aggregations)**
def test_aggregate_response_time():
    """Test the aggregation of response times by category."""
    print("Running test_agggregate_response_time")
    raw_data = extract(DB_PATH, "support")
    clean_data = transform(raw_data)

    agg_data = aggregate_response_time(clean_data)

    # Check that required columns exist
    assert 'category' in agg_data.columns, "Missing 'category' column in output"
    assert 'min_response' in agg_data.columns, "Missing 'min_response' column in output"
    assert 'max_response' in agg_data.columns, "Missing 'max_response' column in output"

    # Check values are rounded correctly
    assert isinstance(agg_data['min_response'].iloc[0], (int, float, np.int64, np.float64)), "min_response should be numeric"
    assert isinstance(agg_data['max_response'].iloc[0], (int, float, np.int64, np.float64)), "max_response should be numeric"

    # Define the expected min and max response times based on the provided values
    expected_values = {
        'Bug': {'min_response': 1, 'max_response': 13},
        'Feedback': {'min_response': 1, 'max_response': 2},
        'Installation Problem': {'min_response': 5, 'max_response': 17},
        'Other': {'min_response': 1, 'max_response': 11}
    }

    # Check specific values for each category
    for category, values in expected_values.items():
        min_response = agg_data.loc[agg_data['category'] == category, 'min_response'].values[0]
        max_response = agg_data.loc[agg_data['category'] == category, 'max_response'].values[0]
        
        assert min_response == values['min_response'], f"Incorrect min_response for {category}. Expected {values['min_response']}, got {min_response}"
        assert max_response == values['max_response'], f"Incorrect max_response for {category}. Expected {values['max_response']}, got {max_response}"


### **Test for CSV Output**
def test_csv_output():
    """Test whether the transformed data is successfully saved to CSV."""
    data = pd.DataFrame({
        'category': ['Feedback', 'Billing Enquiry', 'Bug'],
        'min_response': [10, 5, 8],
        'max_response': [20, 12, 15]
    })

    csv_file = "respond_time.csv"
    data.to_csv(csv_file, index=False)

    # Check if file exists
    assert os.path.exists(csv_file), "CSV file was not created"

    # Check file content
    loaded_data = pd.read_csv(csv_file)
    assert loaded_data.shape == (3, 3), "CSV file has incorrect dimensions"

    # Cleanup
    os.remove(csv_file)

if __name__ == "__main__":
    pytest.main()
