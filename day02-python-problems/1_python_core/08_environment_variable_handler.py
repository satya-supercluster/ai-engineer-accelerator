import os

"""
Problem 8: Environment Variable Handler

Description:
Safely read environment variables with default fallbacks.
Crucial for managing API keys and secrets in production.

Sample Input:
key = 'OPENAI_API_KEY', default = None

Expected Output:
API key value or None
"""

# Your solution here
def get_env_variable(key, default=None):
    """
    Safely read environment variables with default fallbacks.
    
    Args:
        key: The environment variable name
        default: Default value if key is not found
        
    Returns:
        The environment variable value or the default value
    """
    return os.getenv(key, default)


# Example usage
if __name__ == "__main__":
    api_key = get_env_variable('OPENAI_API_KEY', None)
    print(f"API Key: {api_key}")