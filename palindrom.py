txt = input()
""" def palindrom(txt):
    if txt[0] == txt[-1] and len(txt) > 2:
        return palindrom(txt[1:-1])
    elif txt[0] != txt[-1]:
        return 'no'
    return 'yes'
print(palindrom(txt)) """

def is_palindrome(txt):
    if len(txt) < 2:
        return True
    elif txt[0] != txt[-1]:
        return False
    else:
        return is_palindrome(txt[1:-1])
print(is_palindrome(txt))