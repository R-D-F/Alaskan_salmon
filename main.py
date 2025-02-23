import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


with open("nushagak_2020_2024.json", "r") as file:
    full_json_data = json.load(file)
    data = full_json_data["DATA"]


def get_date_no_year(date_time: str) -> str:

    split_date_time = date_time.split(" ")
    date_no_year = split_date_time[0] + " " + split_date_time[1]
    return date_no_year


def get_date_list(data_list: list) -> list:
    "Takes list of json data, returns unique dates"
    dates = []

    for i in data_list:
        date = get_date_no_year(i[1])
        if date not in dates:
            dates.append(date)
    return dates


def get_years_list(json_data: list) -> list:
    years_list = []
    for i in json_data:
        if i[0] not in years_list:
            years_list.append(i[0])
    return years_list


date_list = get_date_list(data)
years_list = get_years_list(data)

num_categories = len(years_list)

fig, ax = plt.subplots()
bars = ax.bar(years_list, np.zeros(num_categories))

ax.set_ylim(0, 1000000)


def update(frame):
    new_values = []
    for i in data:

        if get_date_no_year(i[1]) == date_list[frame]:
            new_values.append(i[2])
    for bar, new_val in zip(bars, new_values):
        bar.set_height(new_val)
    ax.set_title(f"{date_list[frame]}")

    return bars


ani = animation.FuncAnimation(
    fig, update, frames=len(date_list), interval=500, blit=False
)


# total_dict = {}
# for i in data:
#     if i[0] in total_dict:
#         total_dict[i[0]] += i[2]
#     else:
#         total_dict[i[0]] = i[2]

# print(total_dict)


# categories = []
# values = []
# for key, value in total_dict.items():
#     categories.append(key)
#     values.append(value)


# # Create bar graph
# plt.bar(categories, values, color=["blue", "green", "red", "purple", "orange"])

# # Labels and title
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.title("Simple Bar Graph")

# Show the graph
plt.show()
