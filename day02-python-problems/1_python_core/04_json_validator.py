"""
Problem 4: Json Validator

Description:
Validate if a string is valid JSON format.
Critical when working with API responses and LLM outputs.

Sample Input:
json_string = '{"key": "value"}'

Expected Output:
True
"""

# Your solution here
import json
def is_valid_json(json_string):
    """
    Validate if a string is valid JSON format.
    
    Args:
        json_string: String to validate
    
    Returns:
        bool: True if valid JSON, False otherwise
    """
    try:
        json.loads(json_string)
        return True
    except (json.JSONDecodeError, TypeError):
        return False


# Test cases
if __name__ == "__main__":
    print(is_valid_json('{"key": "value"}'))  # True
    print(is_valid_json('[1, 2, 3]'))  # True
    print(is_valid_json('{"invalid": json}'))  # False
    print(is_valid_json('not json'))  # False
    print(is_valid_json(None))  # False
