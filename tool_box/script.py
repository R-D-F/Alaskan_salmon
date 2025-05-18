import arcpy
import json
import os

json_path = r"..\data\json\combined.json"
fc = os.path.abspath(r"..\arc_pro\alaskan_salmon\AWC2024.gdb\AWC\AWC_stream")
fields = ["OID@", "SHAPE@", "NAME"]

# Read JSON data
with open(json_path, "r") as f:
    json_data = json.load(f)

# Output location
gdb = os.path.abspath(r"..\arc_pro\alaskan_salmon\alaskan_salmon.gdb")
output_fc = os.path.join(gdb, "json_table_fc")


# Extract fields from JSON
fields = list(json_data["COLUMNS"])
rows = json_data["DATA"]

arcpy.CreateTable_management(gdb, "json_table_fc")

# Add fields
# TODO detect type:
for field in fields:
    arcpy.AddField_management(
        output_fc, field, "TEXT"
    )  # You can detect type if needed

# Insert rows
with arcpy.da.InsertCursor(output_fc, fields) as cursor:
    for row in rows:
        # TODO convert based on type. add location
        str_row = [str(val) for val in row]  # convert all to string
        cursor.insertRow(str_row)

# with arcpy.da.SearchCursor(fc, fields) as cursor:
#     for row in cursor:
#         print(row[1])
#         break
