import json
import collections


def switch(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(argument, "Invaild month")


with open("34.json", "r") as json_file:
    json_data = json.load(json_file)

birth_list = []

for date in json_data.values():
    month = int(date.split("/")[1])
    month = switch(month)
    birth_list.append(month)

counted = collections.Counter(birth_list)

counted_dict = {}

for counter in counted:
    counted_dict[counter] = counted[counter]
    print("\"{}\": {}".format(counter, counted[counter]))

print(counted_dict)
