dictionary = {}

with open("Training_01.txt", "r") as open_file:
    line = open_file.readline()

    while line:
        category = line.split("/")
        category = category[2]

        if category in dictionary.keys():
            dictionary[category] += 1
        else:
            dictionary[category] = 1

        line = open_file.readline()

print(dictionary)
