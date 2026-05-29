def palindrome(text):

    if text == text[::-1]:
        return True

    return False


print(palindrome("madam"))
