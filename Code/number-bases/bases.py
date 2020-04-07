#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace



def digit_to_ascii(digit):
    return string.printable[digit]

# def to_binary(number):
#     binary_number = []
#     while number >= 1:
#         binary_number.insert(0, number % 2)
#         number = number // 2
#     return binary_number

# def to_binary_recursive(number):
#     if number >= 1:
#         print(number % 2)
#         to_binary_recursive(number // 2)
#     return

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)

    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    # TODO: Decode digits from any base (2 up to 36)

    # ...

    decoded_num = 0
    for i, value in enumerate(digits[::-1]):
        decoded_num += int(value, base) * (base**i)
    return decoded_num





def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)

    # encoded_number = ""
    # while number >= 1:
    #     encoded_number += str(number % 2)
    #     number = number // 2
    
    # return encoded_number[::-1]
    


    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...

    # encoded_number = ''

    # while number >= 1:
    #     encoded_number += str(number % 16)
    #     number = number // 16
    # return encoded_number[::-1]


    # TODO: Encode number in any base (2 up to 36)

    encoded_number = ''

    while number >= 1:
        encoded_number += str(digit_to_ascii(number % base))
        number = number // base
    return encoded_number[::-1]



    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)

    base_10_number = decode(digits, base1)
    converted_number = encode(base_10_number, base2)
    return converted_number

    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')



    # print(decode("f23", 16))
    # print(encode(190, 16))
    # print(convert("111000", 2, 16))
    # print(to_binary_recursive(49))


if __name__ == '__main__':
    main()
    # print(decode('1f', 16))
    # print(encode(45, 2))