"""
Problem 3: Dict Config Parser

Description:
Parse a configuration dictionary and extract nested values safely.
Essential for reading API configurations and model parameters.

Sample Input:
config = {'model': {'name': 'gpt-4', 'temperature': 0.7}}, key = 'model.name'

Expected Output:
'gpt-4'
"""

# Your solution here
def parse_config(config, key, default=None):
    """
    Retrieve a nested value from a dict-like configuration using a dot-separated key.
    Returns default if any part of the path is missing or the path is invalid.
    Supports list indexing with numeric path segments (e.g., "items.0.name").
    """
    if key is None or key == "":
        return config
    current = config
    for part in key.split("."):
        if isinstance(current, dict):
            if part in current:
                current = current[part]
            else:
                return default
        elif isinstance(current, (list, tuple)):
            try:
                idx = int(part)
            except (ValueError, TypeError):
                return default
            if -len(current) <= idx < len(current):
                current = current[idx]
            else:
                return default
        else:
            return default
    return current


if __name__ == "__main__":
    cfg = {"model": {"name": "gpt-4", "temperature": 0.7}, "items": [{"id": 1}, {"id": 2}]}
    print(parse_config(cfg, "model.name"))        # -> 'gpt-4'
    print(parse_config(cfg, "model.temperature")) # -> 0.7
    print(parse_config(cfg, "items.1.id"))        # -> 2
    print(parse_config(cfg, "missing.key", "N/A"))# -> 'N/A'