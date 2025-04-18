import arcpy
import json
import os
from datetime import datetime

fc_path = r"C:\Users\rifra\Homework\Alaskan_salmon\arc_pro\alaskan_salmon\alaskan_salmon.gdb\json_table_fc"

if arcpy.Exists(fc_path):
    arcpy.Delete_management(fc_path)

json_path = r"..\data\json\combined.json"
fc = os.path.abspath(r"..\arc_pro\alaskan_salmon\AWC2024.gdb\AWC\AWC_stream")
fields = ["OID@", "SHAPE@", "NAME"]
name_shape = {}

with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        name_shape[row[2]] = row[1]

field_type_dict = {
    "YEAR": "SHORT",
    "COUNTDATE": "DATE",
    "FISHCOUNT": "LONG",
    "SPECIESID": "SHORT",
    "COUNTLOCATIONID": "SHORT",
    "COUNTLOCATION": "TEXT",
    "SPECIES": "TEXT",
    "GDB_COUNTLOCATION": "TEXT",
    "SHAPE@": "POINT",
}

# Read JSON data
with open(json_path, "r") as f:
    data = json.load(f)

# Output location
gdb = os.path.abspath(r"..\arc_pro\alaskan_salmon\alaskan_salmon.gdb")
output_fc = os.path.join(gdb, "json_table_fc")


# Extract fields from JSON
fields = list(data["COLUMNS"])
fields.append("SHAPE@")
rows = data["DATA"]

arcpy.CreateFeatureclass_management(
    gdb, "json_table_fc", geometry_type="POLYLINE", spatial_reference=fc
)

# Add fields
# TODO detect type:
for field in fields:
    if field == "SHAPE@":
        continue  # SHAPE@ is implicit, don't try to add it manually
    arcpy.AddField_management(
        output_fc, field, field_type_dict[field]
    )  # You can detect type if needed


# Insert rows
def convert_value(value, field_type):
    if value in (None, "", " "):
        return None

    elif field_type == "TEXT":
        return str(value)
    elif field_type in ("SHORT", "LONG"):
        return int(value)
    elif field_type in ("FLOAT", "DOUBLE"):
        return float(value)
    elif field_type == "DATE":

        return datetime.strptime(
            str(value), "%B, %d %Y %H:%M:%S"
        )  # or whatever format you're using
    elif field_type == "POINT":
        return value
    else:
        return value  # fallback


with arcpy.da.InsertCursor(output_fc, fields) as cursor:
    for row in rows:
        gdb_location = row[
            -1
        ]  # Assuming 'GDB_COUNTLOCATION' is the last column
        shape = name_shape.get(gdb_location, None) if gdb_location else None
        row.append(shape)  # Add geometry to row
        converted_row = [
            convert_value(val, field_type_dict[field])
            for val, field in zip(row, fields)
        ]
        cursor.insertRow(converted_row)


# with arcpy.da.SearchCursor(fc, fields) as cursor:
#     for row in cursor:
#         print(row[1])
#         break
