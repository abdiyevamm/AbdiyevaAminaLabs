def count(str):
    resultlow = [x for x in str if x.islower()]
    resultup = [x for x in str if x.isupper()]
    print(f'Number of lower:{len(resultlow)}')
    print(f'Number of lower:{len(resultup)}')


str = input("Enter text:")
count(str)