import json


# json_data = {
#     "name1": "01/01/2020",
#     "name2": "01/01/2020",
#     "name3": "01/01/2020",
#     "name4": "01/02/2020",
#     "name5": "01/02/2020",
#     "name6": "01/03/2020",
#     "name7": "01/04/2020",
#     "name8": "01/05/2020",
#     "name9": "01/06/2020"
# }
#
#
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