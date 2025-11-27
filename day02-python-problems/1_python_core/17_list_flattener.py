"""
Problem 17: List Flattener

Description:
Flatten a nested list into a single level.
Useful when combining results from multiple batch processes.

Sample Input:
[[1, 2], [3, 4], [5]]

Expected Output:
[1, 2, 3, 4, 5]
"""

# Your solution here
def flatten_list(nested_list):
    """Flatten a nested list into a single level."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


# Test with sample input
sample_input = [[1, 2, [4, 6]], [3, 4], [5]]
print(flatten_list(sample_input))  # Output: [1, 2, 4, 6, 3, 4, 5]