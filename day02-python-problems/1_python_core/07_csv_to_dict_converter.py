import csv
from io import StringIO

"""
Problem 7: Csv To Dict Converter

Description:
Convert CSV rows to list of dictionaries.
Common when preparing training data for ML models.

Sample Input:
csv_data with headers: name,age,city

Expected Output:
[{'name': 'John', 'age': '30', 'city': 'NYC'}, ...]
"""

# Your solution here
def csv_to_dict_converter(csv_data):
    """
    Convert CSV data to a list of dictionaries.
    
    Args:
        csv_data (str): CSV data as a string with headers in first row
        
    Returns:
        list: List of dictionaries with headers as keys
    """
    reader = csv.DictReader(StringIO(csv_data))
    return list(reader)


if __name__ == "__main__":
    # Read CSV file
    with open("../../twitter.csv", "r", encoding="utf-8") as f:
        csv_data = f.read()
    
    result = csv_to_dict_converter(csv_data)
    print(result)