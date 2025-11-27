"""
Problem 25: String Similarity Checker

Description:
Check if two strings are similar (basic approach).
Used for fuzzy matching in search and deduplication.

Sample Input:
str1 = 'hello', str2 = 'helo'

Expected Output:
Similarity score
"""

# Your solution here
def string_similarity(str1, str2):
    """Calculate similarity score between two strings using Levenshtein distance."""
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    max_len = max(m, n)
    similarity_score = ((max_len - dp[m][n]) / max_len) * 100
    return round(similarity_score, 2)

# Time Complexity: O(m*n) where m and n are lengths of str1 and str2
# Space Complexity: O(m*n) for the DP table

# Test
str1 = 'hello'
str2 = 'helo'
print(f"Similarity score: {string_similarity(str1, str2)}%")