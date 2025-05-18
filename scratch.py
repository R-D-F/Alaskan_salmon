import json

with open("data\json\combined.json", "r") as f:
    data = json.load(f)

rivers = []
for i in data["DATA"]:
    if i[7] not in rivers:
        rivers.append(i[7])
print(rivers)
