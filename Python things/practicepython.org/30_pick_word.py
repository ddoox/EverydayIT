import random

# my_list = []
# length = 0
# with open("sowpods.txt", "r") as open_file:
#
#     line = open_file.readline()
#     my_list.append(line)
#     while line:
#         length += 1
#         my_list.append(line)
#         line = open_file.readline()


with open("sowpods.txt", "r") as open_file:
    lines = open_file.readlines()


index = random.randint(0, len(lines) + 1)
print(lines[index])
