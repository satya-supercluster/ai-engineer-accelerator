import chardet

"""
Problem 20: Text Encoding Detector

Description:
Detect the encoding of a text string.
Important when reading files with different encodings.

Sample Input:
byte_string = b'\xe2\x9c\x93'

Expected Output:
'utf-8'
"""

# Your solution here
def detect_encoding(byte_string):
    """Detect the encoding of a byte string."""
    result = chardet.detect(byte_string)
    return result['encoding']

# Test with sample input
byte_string = b'\xe2\x9c\x93'
print(detect_encoding(byte_string))

# Test with different encodings
test_cases = [
    b'\xe2\x9c\x93',  # UTF-8
    b'\xff\xfe\x00\x00',  # UTF-32
    b'\xff\xfe',  # UTF-16
    'Hello'.encode('ascii'),  # ASCII
    'Héllo'.encode('latin-1'),  # Latin-1
]

for test in test_cases:
    print(f"{test} -> {detect_encoding(test)}")