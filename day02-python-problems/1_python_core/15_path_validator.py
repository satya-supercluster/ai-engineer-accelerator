import os

"""
Problem 15: Path Validator

Description:
Check if file/directory path exists and is accessible.
Important before reading model files or datasets.

Sample Input:
path = '/path/to/model.pkl'

Expected Output:
True or False
"""

# Your solution here
def validate_path(path):
    """
    Check if a file/directory path exists and is accessible.
    
    Args:
        path: String representing the file or directory path
        
    Returns:
        bool: True if path exists and is accessible, False otherwise
    """
    try:
        return os.path.exists(path) and os.access(path, os.R_OK)
    except (OSError, TypeError):
        return False


# Test with sample input
if __name__ == "__main__":
    path = '/path/to/model.pkl'
    result = validate_path(path)
    print(result)