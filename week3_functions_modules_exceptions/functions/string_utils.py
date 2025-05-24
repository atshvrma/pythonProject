# string_utils.py

def is_palindrome(s):
    """Check if a string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def to_title_case(s):
    """Convert a string to title case."""
    return s.title()

# print(to_title_case("ascs"))