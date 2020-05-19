price_dictionary = {
    "banana": 1.50,
    "avocado": 0.99,
    "heirloom tomato": 0.89,
    "cherry tomato pack": 3.00
}

print("Welcome to the price dictionary. We know the price of:")
for name in price_dictionary.keys():
    print(name)

name = input("\nWho's birthday do you want to look up? ")
if price_dictionary.get(name):
    print("\nPrice of {} is: {}".format(name, price_dictionary.get(name)))   # can't print float, format like printf
else:
    print("Price not found")
