"""
Problem 21: Key Existence Checker

Description:
Safely check if nested keys exist in dictionary.
Prevents KeyError when accessing API response fields.

Sample Input:
data = {'a': {'b': 1}}, keys = ['a', 'b']

Expected Output:
True
"""

# Your solution here
def check_nested_key(data, keys):
    """
    Check if nested keys exist in dictionary.
    
    Args:
        data: Dictionary to search
        keys: List of keys representing the path
    
    Returns:
        True if all keys exist in the nested structure, False otherwise
    """
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return False
    return True


# Test with sample input
data = {'a': {'b': 1}}
keys = ['a', 'b']
print(check_nested_key(data, keys))  # Output: True