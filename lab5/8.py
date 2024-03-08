import re
def split_word(str):
    words = re.split(r'[A-Z]', str)

    word1 = ' '.join(words)

    return word1


str = input("Enter text:")
print(split_word(str))