def conversion(snake_case):
    words = snake_case.split('_')

    camel = words[0]

    for word in words[1:]:
        camel += word.capitalize()

    return camel


str = input("Enter text:")
print(conversion(str))
