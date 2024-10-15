def is_palindrome(s: str) -> bool:
    # Step 1: Clean the string
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Step 2: Check if cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage:
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("race a car"))