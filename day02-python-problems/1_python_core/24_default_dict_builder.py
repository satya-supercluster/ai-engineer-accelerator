"""
Problem 24: Default Dict Builder

Description:
Build dictionary with default values for missing keys.
Useful for configuration management.

Sample Input:
keys = ['model', 'temperature'], default = 'unknown'

Expected Output:
{'model': 'unknown', 'temperature': 'unknown'}
"""

# Your solution here
def build_default_dict(keys, default):
    """Build a dictionary with default values for all keys."""
    return {key: default for key in keys}


# Test with sample input
keys = ['model', 'temperature']
default = 'unknown'
result = build_default_dict(keys, default)
print(result)