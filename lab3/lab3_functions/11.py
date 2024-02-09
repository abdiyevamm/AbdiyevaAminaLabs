# checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
s=input()

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print(is_palindrome(s))