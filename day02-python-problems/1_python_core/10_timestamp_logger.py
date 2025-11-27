from datetime import datetime

"""
Problem 10: Timestamp Logger

Description:
Add timestamps to log messages.
Important for debugging and monitoring LLM applications.

Sample Input:
message = 'Processing request'

Expected Output:
'2024-01-15 10:30:45 - Processing request'
"""

# Your solution here
def timestamp_logger(message):
    """Add timestamp to log message."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} - {message}"

# Test
message = 'Processing request'
print(timestamp_logger(message))