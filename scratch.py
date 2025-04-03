import json
import rapidfuzz

file = r"data\json\combined.json"

locations = []
with open(file, "r") as f:
    data = json.load(f)["DATA"]
    for i in data:
        if i[5] in locations:
            pass
        else:
            locations.append(i[5])

to_fuzz = []
stream_list = r"data\json\streams_list.json"

# print(f"gdb data {locations}")
streams = []
with open(stream_list, "r") as f:
    streams = json.load(f)
    for i in locations:
        if i not in streams:
            to_fuzz.append(i)

for i in to_fuzz:
    best_match = rapidfuzz.process.extractOne(
        i, streams, scorer=rapidfuzz.fuzz.ratio
    )
    print(f"From JSON {i} {best_match}")
    print("\n")
