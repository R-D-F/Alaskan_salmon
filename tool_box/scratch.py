import arcpy
import json
import os
from datetime import datetime

json_path = r"..\data\json\combined.json"
# fc = os.path.abspath(r"..\arc_pro\alaskan_salmon\AWC2024.gdb\AWC\AWC_stream")
# fields = ["OID@", "SHAPE@", "NAME"]

# name_shape = {}

# with arcpy.da.SearchCursor(fc, fields) as cursor:
#     for row in cursor:
#         name_shape[row[2]] = row[1]


# print(name_shape["Klag"])

# with open(json_path, "r") as f:
#     data = json.load(f)

# rows = data["DATA"]

# for i in rows:
#     if not i[-1]:
#         print(i[-1])

x = None
if not x:
    print("TRUE")
else:
    print(False)
