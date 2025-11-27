import sys

"""
Problem 23: Memory Size Calculator

Description:
Calculate approximate memory size of an object.
Important for monitoring memory usage in data processing.

Sample Input:
data = [1, 2, 3, 4, 5]

Expected Output:
Size in bytes
"""

# Your solution here
def calculate_memory_size(obj):
    """
    Calculate the approximate memory size of an object in bytes.
    
    Args:
        obj: Any Python object
        
    Returns:
        int: Size in bytes
    """
    return sys.getsizeof(obj)


# Example usage
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    size = calculate_memory_size(data)
    print(f"Memory size of {data}: {size} bytes")