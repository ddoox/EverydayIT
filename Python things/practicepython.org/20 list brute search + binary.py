def binary(_list, _element):
    found = False

    while len(_list) > 1:
        center = _list[int((len(_list) - 1) / 2)]

        if _element == center:   # has center
            found = True
            break

        elif _element > center:
            _list = _list[int((len(_list) - 1) / 2) + 1::+1]

        else:                   # _element < center
            _list = _list[0:int((len(_list) - 1) / 2):1]

    if _list[0] == _element:
        found = True

    return found


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 33, 88, 95, 123, 456, 789]

number = 33

print(binary(list, number))


# contain = False
#
# for element in list:
#     if element == number:
#         print("yep")
#         contain = True
#         break
#
# if not contain:
#     print("nope")
#

