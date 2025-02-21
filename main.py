import json
import matplotlib.pyplot as plt

with open("nushagak_2020_2024.json", "r") as file:
    json_data = json.load(file)
    data = json_data["DATA"]

total_dict = {}
for i in data:
    if i[0] in total_dict:
        total_dict[i[0]] += i[2]
    else:
        total_dict[i[0]] = i[2]

print(total_dict)


categories = []
values = []
for key, value in total_dict.items():
    categories.append(key)
    values.append(value)


# Create bar graph
plt.bar(categories, values, color=["blue", "green", "red", "purple", "orange"])

# Labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Simple Bar Graph")

# Show the graph
plt.show()
