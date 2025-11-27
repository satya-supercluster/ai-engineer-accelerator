"""
Problem 6: File Line Reader

Description:
Read a large file line by line without loading entire file into memory.
Essential for processing large datasets and logs.

Sample Input:
filename = 'large_data.txt'

Expected Output:
Process each line without memory overflow
"""

# Your solution here
import time
def read_file_line_by_line(filename):
    """
    Read a large file line by line without loading entire file into memory.
    
    Args:
        filename (str): Path to the file to read
        
    Yields:
        str: Each line from the file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.rstrip('\n')
                # wait for 1 second to simulate processing time
                time.sleep(1)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")


# Example usage
if __name__ == "__main__":
    filename = '../../large_text.txt'
    
    # Process each line without loading entire file into memory
    for line_number, line in enumerate(read_file_line_by_line(filename), 1):
        print(f"Line {line_number}: {line}")
        # Process line as needed
