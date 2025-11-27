"""
Problem 12: String Truncator

Description:
Truncate text to maximum length with ellipsis.
Essential for displaying long LLM outputs in UIs.

Sample Input:
text = 'Very long text...', max_length = 20

Expected Output:
'Very long text...'
"""

def truncate_text(text, max_length):
    """
    Truncate text to maximum length with ellipsis.
    
    Args:
        text: The string to truncate
        max_length: Maximum length of the result including ellipsis
    
    Returns:
        Truncated string with ellipsis if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + '...'


# Test
text = 'Very long text that needs truncation'
max_length = 20
print(truncate_text(text, max_length))
