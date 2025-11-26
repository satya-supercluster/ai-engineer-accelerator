import os

# Problem definitions
python_core_problems = [
    {
        "title": "token_counter",
        "description": """Count tokens in a text string by splitting on whitespace.
This is fundamental for understanding LLM token limits.""",
        "input": "text = 'Hello world, this is a test message'",
        "output": "Token count: 7"
    },
    {
        "title": "list_batch_processor",
        "description": """Split a large list into smaller batches of fixed size.
Used for processing data in chunks to avoid memory issues with large datasets.""",
        "input": "data = [1,2,3,4,5,6,7,8,9,10], batch_size = 3",
        "output": "[[1,2,3], [4,5,6], [7,8,9], [10]]"
    },
    {
        "title": "dict_config_parser",
        "description": """Parse a configuration dictionary and extract nested values safely.
Essential for reading API configurations and model parameters.""",
        "input": "config = {'model': {'name': 'gpt-4', 'temperature': 0.7}}, key = 'model.name'",
        "output": "'gpt-4'"
    },
    {
        "title": "json_validator",
        "description": """Validate if a string is valid JSON format.
Critical when working with API responses and LLM outputs.""",
        "input": "json_string = '{\"key\": \"value\"}'",
        "output": "True"
    },
    {
        "title": "string_sanitizer",
        "description": """Remove special characters and extra whitespace from text.
Important for cleaning user input before sending to LLMs.""",
        "input": "text = '  Hello!!!  World???  '",
        "output": "'Hello World'"
    },
    {
        "title": "file_line_reader",
        "description": """Read a large file line by line without loading entire file into memory.
Essential for processing large datasets and logs.""",
        "input": "filename = 'large_data.txt'",
        "output": "Process each line without memory overflow"
    },
    {
        "title": "csv_to_dict_converter",
        "description": """Convert CSV rows to list of dictionaries.
Common when preparing training data for ML models.""",
        "input": "csv_data with headers: name,age,city",
        "output": "[{'name': 'John', 'age': '30', 'city': 'NYC'}, ...]"
    },
    {
        "title": "environment_variable_handler",
        "description": """Safely read environment variables with default fallbacks.
Crucial for managing API keys and secrets in production.""",
        "input": "key = 'OPENAI_API_KEY', default = None",
        "output": "API key value or None"
    },
    {
        "title": "retry_counter",
        "description": """Implement a simple retry mechanism with counter.
Used when API calls fail and need to be retried.""",
        "input": "max_retries = 3, function that might fail",
        "output": "Result after successful retry or exception"
    },
    {
        "title": "timestamp_logger",
        "description": """Add timestamps to log messages.
Important for debugging and monitoring LLM applications.""",
        "input": "message = 'Processing request'",
        "output": "'2024-01-15 10:30:45 - Processing request'"
    },
    {
        "title": "list_deduplicator",
        "description": """Remove duplicate items while preserving order.
Useful for cleaning up repeated results from multiple API calls.""",
        "input": "[1, 2, 2, 3, 1, 4]",
        "output": "[1, 2, 3, 4]"
    },
    {
        "title": "string_truncator",
        "description": """Truncate text to maximum length with ellipsis.
Essential for displaying long LLM outputs in UIs.""",
        "input": "text = 'Very long text...', max_length = 20",
        "output": "'Very long text...'"
    },
    {
        "title": "dict_merger",
        "description": """Merge two dictionaries with conflict resolution.
Used for combining configuration files and model parameters.""",
        "input": "dict1 = {'a': 1}, dict2 = {'b': 2, 'a': 3}",
        "output": "{'a': 3, 'b': 2}"
    },
    {
        "title": "exception_message_extractor",
        "description": """Extract meaningful error messages from exceptions.
Critical for error handling in production systems.""",
        "input": "exception object",
        "output": "Clean error message string"
    },
    {
        "title": "path_validator",
        "description": """Check if file/directory path exists and is accessible.
Important before reading model files or datasets.""",
        "input": "path = '/path/to/model.pkl'",
        "output": "True or False"
    },
    {
        "title": "percentage_calculator",
        "description": """Calculate percentage completion of a task.
Used for showing progress during model training or data processing.""",
        "input": "completed = 45, total = 100",
        "output": "45.0%"
    },
    {
        "title": "list_flattener",
        "description": """Flatten a nested list into a single level.
Useful when combining results from multiple batch processes.""",
        "input": "[[1, 2], [3, 4], [5]]",
        "output": "[1, 2, 3, 4, 5]"
    },
    {
        "title": "null_value_filter",
        "description": """Remove None/null values from a list or dictionary.
Essential for cleaning data before sending to APIs.""",
        "input": "[1, None, 2, None, 3]",
        "output": "[1, 2, 3]"
    },
    {
        "title": "range_validator",
        "description": """Check if a number is within valid range.
Used for validating temperature, top_p, and other LLM parameters.""",
        "input": "value = 0.7, min_val = 0, max_val = 1",
        "output": "True"
    },
    {
        "title": "text_encoding_detector",
        "description": """Detect the encoding of a text string.
Important when reading files with different encodings.""",
        "input": "byte_string = b'\\xe2\\x9c\\x93'",
        "output": "'utf-8'"
    },
    {
        "title": "key_existence_checker",
        "description": """Safely check if nested keys exist in dictionary.
Prevents KeyError when accessing API response fields.""",
        "input": "data = {'a': {'b': 1}}, keys = ['a', 'b']",
        "output": "True"
    },
    {
        "title": "list_rotator",
        "description": """Rotate list elements by n positions.
Useful for round-robin API endpoint selection.""",
        "input": "[1, 2, 3, 4, 5], n = 2",
        "output": "[4, 5, 1, 2, 3]"
    },
    {
        "title": "memory_size_calculator",
        "description": """Calculate approximate memory size of an object.
Important for monitoring memory usage in data processing.""",
        "input": "data = [1, 2, 3, 4, 5]",
        "output": "Size in bytes"
    },
    {
        "title": "default_dict_builder",
        "description": """Build dictionary with default values for missing keys.
Useful for configuration management.""",
        "input": "keys = ['model', 'temperature'], default = 'unknown'",
        "output": "{'model': 'unknown', 'temperature': 'unknown'}"
    },
    {
        "title": "string_similarity_checker",
        "description": """Check if two strings are similar (basic approach).
Used for fuzzy matching in search and deduplication.""",
        "input": "str1 = 'hello', str2 = 'helo'",
        "output": "Similarity score"
    }
]

advanced_python_problems = [
    {
        "title": "async_api_caller",
        "description": """Make multiple async API calls concurrently.
Essential for parallel LLM requests to improve throughput.""",
        "input": "urls = ['api1.com', 'api2.com', 'api3.com']",
        "output": "List of responses from all APIs"
    },
    {
        "title": "decorator_rate_limiter",
        "description": """Create a decorator to rate limit function calls.
Critical for respecting API rate limits (e.g., OpenAI 3 RPM).""",
        "input": "@rate_limit(calls=3, period=60) def api_call()",
        "output": "Function that enforces rate limiting"
    },
    {
        "title": "context_manager_timer",
        "description": """Create a context manager to measure execution time.
Used for profiling LLM API call latency.""",
        "input": "with Timer() as t: # code block",
        "output": "Elapsed time in seconds"
    },
    {
        "title": "lazy_data_loader",
        "description": """Implement a generator for lazy loading large datasets.
Prevents memory overflow when processing millions of records.""",
        "input": "file with 1M rows",
        "output": "Yield one row at a time"
    },
    {
        "title": "thread_pool_executor",
        "description": """Use ThreadPoolExecutor for parallel I/O operations.
Speed up multiple API calls or file operations.""",
        "input": "List of 10 API endpoints to call",
        "output": "All results processed in parallel"
    },
    {
        "title": "custom_exception_hierarchy",
        "description": """Design a custom exception hierarchy for error handling.
Properly categorize errors in LLM applications (APIError, ValidationError, etc.).""",
        "input": "Base exception class and specific error types",
        "output": "Structured exception handling"
    },
    {
        "title": "lru_cache_implementation",
        "description": """Implement or use LRU cache for expensive computations.
Cache LLM embeddings to avoid recomputation.""",
        "input": "Function that generates embeddings",
        "output": "Cached results for repeated inputs"
    },
    {
        "title": "metaclass_registry",
        "description": """Use metaclass to create a plugin registry.
Dynamically register different LLM providers (OpenAI, Anthropic, etc.).""",
        "input": "Base LLM class",
        "output": "Auto-register all LLM provider subclasses"
    },
    {
        "title": "property_validator",
        "description": """Create properties with validation using @property decorator.
Validate LLM parameters like temperature before setting.""",
        "input": "class Config: temperature setter with validation",
        "output": "Raise error if temperature not in [0, 1]"
    },
    {
        "title": "dataclass_config",
        "description": """Use dataclasses for type-safe configuration objects.
Structure LLM API configurations with type hints.""",
        "input": "@dataclass with model_name, temperature, max_tokens",
        "output": "Type-safe config object"
    },
    {
        "title": "enum_model_types",
        "description": """Create Enum for model types and parameters.
Type-safe way to handle different model names and versions.""",
        "input": "Enum for GPT3, GPT4, Claude, etc.",
        "output": "Prevent invalid model name strings"
    },
    {
        "title": "abstract_base_class",
        "description": """Define abstract base class for LLM providers.
Enforce interface contract for different LLM implementations.""",
        "input": "ABC with abstract methods: generate(), embed()",
        "output": "Force subclasses to implement required methods"
    },
    {
        "title": "singleton_connection_pool",
        "description": """Implement singleton pattern for connection pooling.
Reuse HTTP sessions across multiple API calls.""",
        "input": "ConnectionPool class",
        "output": "Single shared instance across application"
    },
    {
        "title": "descriptor_protocol",
        "description": """Use descriptor protocol for computed attributes.
Automatically format or validate attributes on access.""",
        "input": "class Validated: descriptor for bounded values",
        "output": "Attribute with custom get/set logic"
    },
    {
        "title": "protocol_typing",
        "description": """Use Protocol from typing for structural subtyping.
Define interfaces without inheritance for flexible LLM clients.""",
        "input": "Protocol with generate() method signature",
        "output": "Type checking without explicit inheritance"
    },
    {
        "title": "generic_types",
        "description": """Create generic classes using TypeVar.
Type-safe response wrappers for different API return types.""",
        "input": "class Response[T]: with generic type parameter",
        "output": "Response[str], Response[dict], etc."
    },
    {
        "title": "async_context_manager",
        "description": """Create async context manager for resource handling.
Properly manage async database or API connections.""",
        "input": "async with AsyncClient() as client:",
        "output": "Automatic async setup/teardown"
    },
    {
        "title": "weak_reference_cache",
        "description": """Use weakref for cache that doesn't prevent garbage collection.
Cache embeddings without causing memory leaks.""",
        "input": "WeakValueDictionary for embedding cache",
        "output": "Cache that auto-clears unused entries"
    },
    {
        "title": "functools_partial",
        "description": """Use functools.partial for function configuration.
Pre-configure API call functions with common parameters.""",
        "input": "partial(api_call, model='gpt-4', temperature=0.7)",
        "output": "Function with preset parameters"
    },
    {
        "title": "itertools_combinations",
        "description": """Use itertools for efficient iteration patterns.
Generate combinations for hyperparameter tuning.""",
        "input": "temperatures = [0.5, 0.7, 0.9], top_p = [0.9, 0.95]",
        "output": "All combinations efficiently"
    },
    {
        "title": "slots_optimization",
        "description": """Use __slots__ to reduce memory footprint.
Optimize memory for classes with millions of instances.""",
        "input": "class Token: with __slots__",
        "output": "Reduced memory per instance"
    },
    {
        "title": "pickle_serialization",
        "description": """Serialize and deserialize complex objects with pickle.
Save trained models or processed data to disk.""",
        "input": "model_object",
        "output": "Saved to file and loaded back"
    },
    {
        "title": "multiprocessing_pool",
        "description": """Use multiprocessing for CPU-bound parallel tasks.
Process multiple documents for embeddings in parallel.""",
        "input": "List of 1000 documents to process",
        "output": "Processed using all CPU cores"
    },
    {
        "title": "queue_based_worker",
        "description": """Implement producer-consumer pattern with Queue.
Process LLM requests from queue with worker threads.""",
        "input": "Queue with pending requests",
        "output": "Multiple workers processing from queue"
    },
    {
        "title": "namespace_management",
        "description": """Use types.SimpleNamespace for flexible config objects.
Create dynamic configuration from dictionary.""",
        "input": "config_dict = {'model': 'gpt-4', 'temp': 0.7}",
        "output": "config.model, config.temp accessible"
    }
]

def create_problem_files(category, problems, base_path):
    """Create folder structure and problem files."""
    category_path = os.path.join(base_path, category)
    os.makedirs(category_path, exist_ok=True)
    
    for idx, problem in enumerate(problems, 1):
        # Create problem file
        filename = f"{idx:02d}_{problem['title']}.py"
        filepath = os.path.join(category_path, filename)
        
        # Write problem content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f'"""\n')
            f.write(f"Problem {idx}: {problem['title'].replace('_', ' ').title()}\n\n")
            f.write(f"Description:\n{problem['description']}\n\n")
            f.write(f"Sample Input:\n{problem['input']}\n\n")
            f.write(f"Expected Output:\n{problem['output']}\n")
            f.write(f'"""\n\n')
            f.write(f"# Your solution here\n")
    
    print(f"✓ Created {len(problems)} problems in {category}/")

def main():
    base_path = "ai_engineer_python_problems"
    
    # Create base directory
    os.makedirs(base_path, exist_ok=True)
    
    # Create README
    with open(os.path.join(base_path, "README.md"), 'w', encoding='utf-8') as f:
        f.write("# AI Engineer Python Problem Set\n\n")
        f.write("This problem set covers essential Python concepts for AI Software Engineers.\n\n")
        f.write("## Structure\n\n")
        f.write("### 1. Python Core (25 problems)\n")
        f.write("Fundamental concepts essential for data processing, API interactions, and basic automation.\n\n")
        f.write("### 2. Advanced Python (25 problems)\n")
        f.write("Advanced patterns for performance, concurrency, type safety, and professional software engineering.\n\n")
        f.write("## How to Use\n\n")
        f.write("1. Start with Python Core problems (01-25)\n")
        f.write("2. Progress to Advanced Python problems (01-25)\n")
        f.write("3. Each file contains the problem description, sample input/output\n")
        f.write("4. Write your solution below the comments\n")
        f.write("5. Test your solution with different inputs\n\n")
        f.write("## Key Focus Areas\n\n")
        f.write("- API integration and error handling\n")
        f.write("- Data processing and transformation\n")
        f.write("- Memory management and optimization\n")
        f.write("- Async/concurrent programming\n")
        f.write("- Type safety and code quality\n")
        f.write("- Real-world LLM/ML engineering scenarios\n")
    
    # Create problem files
    create_problem_files("1_python_core", python_core_problems, base_path)
    create_problem_files("2_advanced_python", advanced_python_problems, base_path)
    
    print(f"\n✅ Successfully created problem set in '{base_path}/' directory")
    print(f"\n📊 Summary:")
    print(f"   - Python Core: 25 problems")
    print(f"   - Advanced Python: 25 problems")
    print(f"   - Total: 50 problems")
    print(f"\n🚀 Start with: {base_path}/1_python_core/01_token_counter.py")

if __name__ == "__main__":
    main()