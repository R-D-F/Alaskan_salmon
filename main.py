import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


with open(r"data\json\combined.json", "r") as file:
    full_json_data = json.load(file)
    print(full_json_data[0])


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
print(date_list)
years_list = get_years_list(data)

num_categories = len(years_list)

fig, ax = plt.subplots()
bars = ax.bar(years_list, np.zeros(num_categories))

ax.set_ylim(0, 6000000)

year_totals = {x: 0 for x in years_list}


def update(frame):
    print(frame)
    new_values = []
    for i in data:

        if get_date_no_year(i[1]) == date_list[frame]:
            year_totals[i[0]] += i[2]
    for k, v in year_totals.items():
        new_values.append(v)
    for bar, new_val in zip(bars, new_values):
        bar.set_height(new_val)
    ax.set_title(f"{date_list[frame]}")

    # If the last frame is reached, stop the animation
    if frame == len(date_list) - 1:
        ani.event_source.stop()

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
