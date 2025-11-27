"""
Problem 2: List Batch Processor

Description:
Split a large list into smaller batches of fixed size.
Used for processing data in chunks to avoid memory issues with large datasets.

Sample Input:
data = [1,2,3,4,5,6,7,8,9,10], batch_size = 3

Expected Output:
[[1,2,3], [4,5,6], [7,8,9], [10]]
"""

# Your solution here
list_input = input("Enter a list of numbers separated by commas: ")
data = [int(x) for x in list_input.split(",")]
batch_size = int(input("Enter the batch size: "))
# batched_data = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
batched_data = []
for i in range(0,len(data), batch_size):
    batched_data.append(data[i:i+batch_size])
print(batched_data)


#######################################################
# Suggested by AI
from typing import List, TypeVar

T = TypeVar('T')

def batch_list(data: List[T], batch_size: int) -> List[List[T]]:
    """Split a list into batches of specified size."""
    if batch_size <= 0:
        raise ValueError("Batch size must be positive")
    
    return [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

def main():
    try:
        list_input = input("Enter numbers separated by commas: ").strip()
        
        if not list_input:
            print("Empty input. Result: []")
            return
        
        data = [int(x.strip()) for x in list_input.split(",")]
        batch_size = int(input("Enter the batch size: "))
        
        batched_data = batch_list(data, batch_size)
        print(batched_data)
        
    except ValueError as e:
        print(f"Error: Invalid input - {e}")

if __name__ == "__main__":
    main()

# Key improvements:

# Use the list comprehension (it's cleaner and more Pythonic)
# Added error handling for invalid inputs
# Added validation for batch_size (must be positive)
# Use strip() on each number to handle extra whitespace
# Made the batching function generic with TypeVar for type safety
# Separated logic into reusable function
# Better variable naming and structure

# Optional Enhancement - Using itertools for memory efficiency with large datasets:
from itertools import islice
from typing import Iterator, List, TypeVar

T = TypeVar('T')

def batch_iterable(iterable: List[T], batch_size: int) -> Iterator[List[T]]:
    """Memory-efficient batching using itertools."""
    it = iter(iterable)
    while batch := list(islice(it, batch_size)):
        yield batch