#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    start = 0
    end = 0
    
    if pattern == '': # If pattern in empty return True
        return True

    while (start+end) < len(text):
        if text[start+end] != pattern[end]:
            start += 1 # Moving text pointer to next letter
            end = 0 # Resetting end to be 0, moment match not found
            continue
        else: # There is a match so move the pointer down
            end += 1
        
        if end == len(pattern): # If the end count is equal to pattern then all matches
            return True

    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    start = 0
    end = 0

    if pattern == '': # If pattern empty return 0
        return 0

    while (start+end) < len(text):
        if text[start+end] != pattern[end]:
            start += 1
            end = 0
            continue
        else:
            end += 1
        
        if end == len(pattern): # They all matches so return the start which is index
            return start


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    list_match_indexes = []
    start = 0
    end = 0

    if pattern == '': # If pattern empty return list of all indexes of text
        for i in range(len(text)):
            list_match_indexes.append(i)
        return list_match_indexes

    while (start+end) < len(text):
        if text[start+end] != pattern[end]:
            start += 1
            end = 0
            continue
        else:
            end += 1
        
        if end == len(pattern): # They all matches so return the start which is index
            list_match_indexes.append(start)
            # To handle overlapping patterns
            if end > 1: 
                same = 0 # Get number of overlapping instances
                for i in range(end-1):
                    if pattern[i] == pattern[i+1]:
                        same += 1
                start += end - same # Set start to be back however many overlapping is seen
                end = 0

            # Else if end == 1 to just move start to next letter in text
            start += end # Move start pointer of text to after the match
            end = 0 # To reset end point for the pattern, to look for another pattern in text

    return list_match_indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
