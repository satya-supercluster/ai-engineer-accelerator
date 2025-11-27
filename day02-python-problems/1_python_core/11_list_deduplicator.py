"""
Problem 11: List Deduplicator

Description:
Remove duplicate items while preserving order.
Useful for cleaning up repeated results from multiple API calls.

Sample Input:
[1, 2, 2, 3, 1, 4]

Expected Output:
[1, 2, 3, 4]
"""

# Your solution here
def deduplicate_list(items):
    """Remove duplicates while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# Test with sample input
sample_input = [1, 2, 2, 3, 1, 4]
print(deduplicate_list(sample_input))  # Output: [1, 2, 3, 4]