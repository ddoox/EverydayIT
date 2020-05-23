def op():
    _file = open("file.txt")
    return _file


# file = op()
# print(file.read())  #everything
# file.close()

# file = op()
# print(file.readline())  # one line
# file.close()

file = op()
print(file.readlines())  #lines in list
file.close()

