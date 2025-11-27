import random

"""
Problem 9: Retry Counter

Description:
Implement a simple retry mechanism with counter.
Used when API calls fail and need to be retried.

Sample Input:
max_retries = 3, function that might fail

Expected Output:
Result after successful retry or exception
"""

# Your solution here
def retry_with_counter(func, max_retries=3, *args, **kwargs):
    """
    Retry a function call up to max_retries times.
    
    Args:
        func: Function to retry
        max_retries: Maximum number of retry attempts
        *args: Positional arguments for func
        **kwargs: Keyword arguments for func
    
    Returns:
        Result of successful function call
    
    Raises:
        Exception: If all retries fail
    """
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            retry_count += 1
            if retry_count >= max_retries:
                print(f"Failed after {max_retries} attempts")
                raise
            print(f"Attempt {retry_count} failed: {str(e)}. Retrying...")
    
    return None


# Example usage
def unreliable_api_call():
    if random.random() < 0.7:
        raise Exception("API call failed")
    return "Success!"


if __name__ == "__main__":
    try:
        result = retry_with_counter(unreliable_api_call, max_retries=3)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Final Exception: {str(e)}")