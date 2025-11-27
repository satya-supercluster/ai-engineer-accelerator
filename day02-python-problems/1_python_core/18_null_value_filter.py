"""
Problem 18: Null Value Filter

Description:
Remove None/null values from a list or dictionary.
Essential for cleaning data before sending to APIs.

Sample Input:
[1, None, 2, None, 3]

Expected Output:
[1, 2, 3]
"""

# Your solution here
def filter_null_values(data):
    """Remove None/null values from a list or dictionary."""
    if isinstance(data, list):
        return [item for item in data if item is not None]
    elif isinstance(data, dict):
        return {key: value for key, value in data.items() if value is not None}
    return data


# Test with sample input
sample_input = [1, None, 2, None, 3]
print(filter_null_values(sample_input))