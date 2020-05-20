import json


# json_data = {
#     "name1": "date1",
#     "name2": "date2",
#     "name3": "date3",
#     "name4": "date4",
#     "name5": "date5",
#     "name6": "date6",
#     "name7": "date7",
#     "name8": "date8,",
#     "name9": "date9"
# }


# with open("34.json", "w") as json_file:
#     json.dump(json_data, json_file)   # auto convert False -> false
#
# print(json_data.keys())


with open("34.json", "r") as json_file:
    json_data = json.load(json_file)

    print("Welcome to the price dictionary. We know the price of:")
    for name in json_data.keys():
        print(name)

    name = input("\nWho's birthday do you want to look up? ")
    if json_data.get(name):
        print("\nPrice of {} is: {}".format(name, json_data.get(name)))   # can't print float, format like printf
    else:
        print("Price not found")