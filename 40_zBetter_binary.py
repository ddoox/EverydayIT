# TODO: complete in free time
def binary(_list, _element):
    found = False
    start_index = 1
    end_index = len(_list) - 1

    while 1:

        center_index = (end_index - start_index)/2

        element_from_center = int(_list[center_index])

        if _element == element_from_center:  # has center
            found = True
            break

        elif _element > element_from_center:
            end_index = center_index

        else:                                # _element < center
            start_index = center_index

        if center_index < start_index or center_index > end_index or center_index < 0:
            break

    if _list[0] == _element:
        found = True

    return found


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 33, 88, 95, 123, 456, 789]

number = 33

print(binary(list, number))
