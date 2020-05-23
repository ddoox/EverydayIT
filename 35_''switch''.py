import json


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


birthday_dict = {}

with open("34.json", "r") as json_file:
    json_data = json.load(json_file)

for date in json_data.values():
    month = int(date.split("/")[1])
    month = switch(month)

    if month in birthday_dict.keys():
        birthday_dict[month] += 1
    else:
        birthday_dict[month] = 1

with open("35.json", "w") as json_file:
    json.dump(birthday_dict, json_file)