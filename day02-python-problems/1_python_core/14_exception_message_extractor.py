"""
Problem 14: Exception Message Extractor

Description:
Extract meaningful error messages from exceptions.
Critical for error handling in production systems.

Sample Input:
exception object

Expected Output:
Clean error message string
"""

# Your solution here
def extract_exception_message(exception):
    """
    Extract meaningful error message from an exception object.
    
    Args:
        exception: An exception object
        
    Returns:
        str: Clean error message
    """
    # Get the exception message
    message = str(exception)
    
    # Return the message, or a default if empty
    return message if message else type(exception).__name__


# Example usage
if __name__ == "__main__":
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        print(extract_exception_message(e))  # Output: division by zero
    
    try:
        data = {"key": "value"}
        print(data["missing"])
    except KeyError as e:
        print(extract_exception_message(e))  # Output: 'missing'
    
    try:
        int("not a number")
    except ValueError as e:
        print(extract_exception_message(e))  # Output: invalid literal for int() with base 10: 'not a number'