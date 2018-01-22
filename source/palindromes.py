#!python
import pdb
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
    #first filter out punctuation, actually, we may not even need to, we can just check if its an integer or char
    #Now we we make all the letters lowercase

    text = text.replace(" ", "")
    normal_text = ""
    reversed_text = ""
    for index in text:
        if index not in string.punctuation:
            normal_text += index.lower()
    #now we have all our letters
    for index in reversed(normal_text):
        if index not in string.punctuation:
            reversed_text += index
    if normal_text == reversed_text:
        return True
    else:
        return False


    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here

    #Right now, the recursive function is returning more than 1 False I think, thats why its messing up
    #what we should do is set a value to true or false, and then return that value

    #cleaning stuff only in the beginning
    if left == None and right == None:
        normal_text = ""
        text = text.replace(" ", "")

        #Make everything lower case first
        for index in text:
            if index not in string.punctuation:
                normal_text += index.lower()
        #This is for the first time the function is ran, when left and right is None

        left = 0

        right = len(text) - 1
        text = normal_text

    #If theres only one character left we should return True
    pdb.set_trace()
    if left == right:
        return True
    #If the selected characters do not equal each other, it's false
    elif left < right:
        if text[left] != text[right]:
            return False
        else:
            is_palindrome_recursive(text, left + 1, right - 1)

    return True






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
