import json

file = r"data\json\combined.json"

locations = []
with open(file, "r") as f:
    data = json.load(f)["DATA"]
    for i in data:
        if i[5] in locations:
            pass
        else:
            locations.append(i[5])

in_both = []
stream_list = r"data\json\streams_list.json"
with open(stream_list, "r") as f:
    streams = json.load(f)
    for i in locations:
        if i in streams:
            in_both.append(i)


for i in locations:
    if i not in in_both:
        print(i)
