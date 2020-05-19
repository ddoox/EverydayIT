import json

#TODO: do some things with it
json_data = {
    "name": "Michele",
    "shirt_color": "blue",
    "laptops": [{
        "brand": "Lenovo",
        "operating_system": "Ubuntu"
    },
        {
            "brand": "Apple",
            "operating_system": "OSX"
        }
    ],
    "has_a_dog": False,
    "items_on_desk": ["mug", "pen", "monitor"]
}

with open("34.json", "w") as json_file:
    json.dump(json_data, json_file)   # auto convert False -> false

print(json_data.keys())

