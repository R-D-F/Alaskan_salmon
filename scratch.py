import json
import rapidfuzz

print("this is working too")

# file = r"data\json\combined.json"

# json_streams = []
# with open(file, "r") as f:
#     data = json.load(f)["DATA"]
#     for i in data:
#         if i[5] in json_streams:
#             pass
#         else:
#             json_streams.append(i[5])

# to_fuzz = []
# stream_list = r"data\json\streams_list.json"

# # print(f"gdb data {json_streams}")
# gdb_streams = []
# with open(stream_list, "r") as f:
#     gdb_streams = json.load(f)
#     for i in json_streams:
#         if i not in gdb_streams:
#             to_fuzz.append(i)

# # no_match_dict = {}
# # for i in to_fuzz:
# #     best_match = rapidfuzz.process.extractOne(
# #         i, gdb_streams, scorer=rapidfuzz.fuzz.ratio
# #     )

# #     no_match_dict[i] = best_match[0]
# #     print(f"From JSON {i} {best_match}")
# #     print("\n")
# #     print(no_match_dict)

# x = {
#     "Afognak River (Litnik)": "Afognak River",
#     "Copper River (Miles L)": "Copper River",
#     "Deshka": "Deshka River / Kroto Creek",
#     "Jim Creek": "Jims Creek",
#     "Kasilof River (sockeye)": "Kasilof River",
#     "Kenai River (Chinook)": "Kenai River",
#     "Kenai River (late-run sockeye)": "Kandik River",
#     "Klag": None,
#     "Little Susitna": "Little Susitna River",
#     "McLees Lake": None,
#     "Nelson River (Sapsuk)": "Necons River",
#     "Olga Creek (Upper Station)": "Olga Creek",
#     "Orzinski Lake": None,
#     "Pasagshak": "*Pasagshak River",
#     "Pauls Bay River": None,
#     "Redoubt Lake": None,
# }

# with open(file, "r") as f:
#     data = json.load(f)

# # Add new column
# new_column = "GDB_COUNTLOCATION"
# data["COLUMNS"].append(new_column)

# # Add default value to each data row
# for row in data["DATA"]:
#     if row[5] in gdb_streams:
#         row.append(row[5])
#     else:
#         row.append(x[row[5]])

# # Save it back
# with open(file, "w") as f:
#     json.dump(data, f, indent=4)
