"""
Problem 19: Range Validator

Description:
Check if a number is within valid range.
Used for validating temperature, top_p, and other LLM parameters.

Sample Input:
value = 0.7, min_val = 0, max_val = 1

Expected Output:
True
"""

# Your solution here
def is_in_range(value, min_val, max_val):
    """
    Check if a number is within valid range (inclusive).
    
    Args:
        value: The number to validate
        min_val: Minimum allowed value
        max_val: Maximum allowed value
    
    Returns:
        True if value is within range, False otherwise
    """
    return min_val <= value <= max_val


# Test with the sample input
value = 0.7
min_val = 0
max_val = 1
print(is_in_range(value, min_val, max_val))  # Output: True