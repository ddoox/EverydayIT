# input_file = [1,1,1,4,99,5,6,0,99]
with open("input", "r") as input_file:
    input_file = input_file.read()
    input_file = input_file.strip().split(",")
    swap = []

    for number in input_file:
        swap.append(int(number))
input_file = swap

print(input_file)

vv = 0
nn = 0
found = False

# for noun in range(0, 100):
#     for verb in range(0, 100):
#         with open("input", "r") as input_file:
#             input_file = input_file.read()
#             input_file = input_file.strip().split(",")
#             swap = []
#
#             for number in input_file:
#                 swap.append(int(number))
#
#         input_file = swap
#         input_file[1] = noun
#         input_file[2] = verb
#
result_index = 0
opcode = 0
#         print(input_file)

while input_file[opcode] == 1 or input_file[opcode] == 2:
    if input_file[opcode] == 1:
        result_index = input_file[opcode + 3]
        input_file[result_index] = input_file[input_file[opcode + 1]] + input_file[input_file[opcode + 2]]
        opcode += 4
    if input_file[opcode] == 2:
        result_index = input_file[opcode + 3]
        input_file[result_index] = input_file[input_file[opcode + 1]] * input_file[input_file[opcode + 2]]
        opcode += 4
#
# if input_file[opcode] == 99:
#     if input_file[0] == 19690720:
#         found = True
#         vv = verb * 100
#         nn = noun
#         break


        # if input_file[0] == 19690720:
        #     print(noun)
        # input_file = swap
        # if input_file[0] == 19690720:
        #     print(noun * 100 + verb)
        #     break
        # else:
        #     input_file = swap

    # if input_file[0] == 19690720:
    #     print(noun * 100 + verb)
    #     break
    # else:
    #     input_file = swap

# print(input_file)
