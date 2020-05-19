def uniq(list):
    new = [element for element in set(list)]
    return new


a = [1, 1, 2, 2, 3, 3, 4, 4]

print(uniq(a))