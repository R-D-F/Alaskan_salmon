import json

file = r"data\json\raw\Afognak River (Litnik)_Chinook.json"

combined_data = []

with open(file, "r", encoding="utf-8") as f:
    data = json.load(f)
    # print(data["DATA"])
    combined_data.append(data["DATA"])

with open(r"data\json\combined.json", "w", encoding="utf-8") as f:
    json.dump(combined_data[0], f, indent=4)
