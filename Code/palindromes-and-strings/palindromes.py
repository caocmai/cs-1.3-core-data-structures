#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)

    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    cleaned_string = ''
    # Cleaning the string to have only characters
    for letter in text.lower():
      if string.ascii_lowercase.find(letter) >= 0:
          cleaned_string += letter

    left_index = 0
    right_index = len(cleaned_string) - 1
    
    # Loop through string, dividing 1/2 each time and see if they don't match then break out loop return False
    while left_index < right_index:
      if cleaned_string[left_index] != cleaned_string[right_index]:
        return False
      left_index += 1
      right_index -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests
    cleaned_string = ''
    # Cleaning the string to have only characters
    for letter in text.lower():
      if string.ascii_lowercase.find(letter) >= 0:
          cleaned_string += letter
    # If left and right None then set then to be 0, and lenth of string - 1 respectively
    if left is None and right is None:
        left = 0
        right = len(cleaned_string) - 1

    # Three base cases
    if len(cleaned_string) == 0: # This if the string is empty
        return True
    elif cleaned_string[left] != cleaned_string[right]:
        return False
    elif right == 0:
        return True
    else:
        return is_palindrome_recursive(cleaned_string, left+1, right-1) # Left pointer moves up, right down

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
