"""
Problem 22: List Rotator

Description:
Rotate list elements by n positions.
Useful for round-robin API endpoint selection.

Sample Input:
[1, 2, 3, 4, 5], n = 2

Expected Output:
[4, 5, 1, 2, 3]
"""

# Your solution here
def rotate_list(lst, n):
    """Rotate list elements by n positions to the left."""
    if not lst:
        return lst
    n = n % len(lst)  # Handle n larger than list length
    return lst[n:] + lst[:n]


# Test with the sample input
result = rotate_list([1, 2, 3, 4, 5], 2)
print(result)  # Output: [3, 4, 5, 1, 2]