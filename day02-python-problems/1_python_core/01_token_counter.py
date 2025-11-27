"""
Problem 1: Token Counter

Description:
Count tokens in a text string by splitting on whitespace.
This is fundamental for understanding LLM token limits.

Sample Input:
text = 'Hello world, this is a test message'

Expected Output:
Token count: 7
"""

# Your solution here
text: str = input("Enter the text: ")
tokens = text.split(" ")
print(f"Token count: {len(tokens)}")



#######################################################
# Suggested by AI
def count_tokens(text: str) -> int:
    """Count tokens by splitting on any whitespace."""
    return len(text.split())

def main():
    text = input("Enter the text: ").strip()
    
    if not text:
        print("Token count: 0")
        return
    
    token_count = count_tokens(text)
    print(f"Token count: {token_count}")

if __name__ == "__main__":
    main()

# Key improvements:

# Use split() without arguments to split on any whitespace (spaces, tabs, newlines, multiple spaces)
# Added function for reusability and testability
# Handle empty input gracefully
# Use strip() to remove leading/trailing whitespace
# Added proper main guard