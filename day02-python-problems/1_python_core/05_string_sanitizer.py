"""
Problem 5: String Sanitizer

Description:
Remove special characters and extra whitespace from text.
Important for cleaning user input before sending to LLMs.

Sample Input:
text = '  Hello!!!  World???  '

Expected Output:
'Hello World'
"""

# Your solution here
import re
def sanitize_string(text):
    """Remove special characters and extra whitespace from text."""
    # Remove special characters, keep only alphanumeric and spaces
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Remove extra whitespace
    cleaned = ' '.join(cleaned.split())
    return cleaned


# Test with sample input
text = '  Hello!!!  World???  '
result = sanitize_string(text)
print(result)  # Output: Hello World