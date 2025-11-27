"""
Problem 16: Percentage Calculator

Description:
Calculate percentage completion of a task.
Used for showing progress during model training or data processing.

Sample Input:
completed = 45, total = 100

Expected Output:
45.0%
"""

# Your solution here
completed = 45
total = 100
percentage = (completed / total) * 100
print(f"{percentage}%")