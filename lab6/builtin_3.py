def isPalindrome(str):
    str1 = str[0:int((len(str)/2))]
    str2 = str[len(str):int((len(str) - 1)/2):-1]
    if str1 == str2:
        print("Palindrome")
    else:
        print("is not Palindrome")

str = input("Enter text:")
isPalindrome(str)