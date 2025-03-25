import os
import json

path = os.path.dirname(os.path.abspath(__file__))

folder = r"data\json\raw"

json_files = os.listdir(folder)
json_files_full_path = []
for file in json_files:
    json_files_full_path.append(os.path.join(path, folder, file))


# Initialize a list to store the combined data
combined_dict = {
    "COLUMNS": [
        "YEAR",
        "COUNTDATE",
        "FISHCOUNT",
        "SPECIESID",
        "COUNTLOCATIONID",
        "COUNTLOCATION",
        "SPECIES",
    ],
    "DATA": [],
}

for file in json_files_full_path:
    with open(file, "r", encoding="utf-8") as f:
        full_dict = json.load(f)

        data = full_dict["DATA"]

        if isinstance(data, list):
            combined_dict["DATA"].extend(data)  # Append lists
        else:
            combined_dict["DATA"].append(data)  # Append objects

# Save combined data to a new JSON file
with open("combined.json", "w", encoding="utf-8") as f:
    json.dump(combined_dict, f, indent=4)
