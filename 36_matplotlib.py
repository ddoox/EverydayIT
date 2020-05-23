import matplotlib.pyplot as plt
import json


birthday_dict = {}

with open("35_2.json", "r") as json_file:
    json_data = json.load(json_file)
# print(json_data[January])


#   -   -   -   plot    -   -   -   #
plot_x = []
plot_y = []

for element in json_data:
    plot_x.append(element)
    plot_y.append(json_data[element])

plt.plot(plot_x, plot_y)
plt.show()
