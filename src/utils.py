import pandas as pd

def check_data_quality(df):
    """
    Performs a basic data quality check:
    - shape
    - null values
    - data types
    - unique values (categorical)
    - numeric stats
    - duplicates
    """
    print("=== DATA QUALITY CHECK ===\n")
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")

    print("Null values per column:\n", df.isnull().sum(), "\n")

    print("Data types:\n", df.dtypes, "\n")

    for col in df.select_dtypes(include=["object"]).columns:
        print(f"Unique values in '{col}':\n", df[col].unique(), "\n")

    print("Descriptive statistics (numeric columns):\n", df.describe(), "\n")

    dups = df.duplicated().sum()
    print(f"Duplicate rows: {dups}")
    print("No duplicates.\n" if dups == 0 else "Consider using df.drop_duplicates().\n")



def normalize_column(df, col_name):
    """
    Removes leading/trailing spaces and capitalizes the first letter of each word.
    Useful for cleaning categorical text columns.
    """
    df[col_name] = df[col_name].str.strip().str.title()
    return df


def filter_outliers(df, col_name, min_val, max_val):
    """
    Filters rows based on a numeric column range.
    Keeps values between min_val and max_val (inclusive).
    """
    return df[(df[col_name] >= min_val) & (df[col_name] <= max_val)]
