"""
Problem 13: Dict Merger

Description:
Merge two dictionaries with conflict resolution.
Used for combining configuration files and model parameters.

Sample Input:
dict1 = {'a': 1}, dict2 = {'b': 2, 'a': 3}

Expected Output:
{'a': 3, 'b': 2}
"""

# Your solution here
def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries with dict2 values taking precedence on conflicts.
    
    Args:
        dict1: First dictionary
        dict2: Second dictionary (values override dict1 on conflict)
    
    Returns:
        Merged dictionary with dict2 values taking precedence
    """
    result = dict1.copy()
    result.update(dict2)
    return result


# Test with sample input
dict1 = {'a': 1}
dict2 = {'b': 2, 'a': 3}
print(merge_dicts(dict1, dict2))  # Output: {'a': 3, 'b': 2}