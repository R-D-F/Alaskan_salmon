import arcpy
import json

# Set workspace
feature_class = r"alaskan_salmon\AWC2024.gdb\AWC\AWC_stream"

# Define the fields you want to check (use ["*"] for all fields)
fields = ["NAME"]
names = []

# Open a search cursor
with arcpy.da.SearchCursor(feature_class, fields) as cursor:
    for row in cursor:
        if row[0] in names:
            pass
        else:
            names.append(row[0])
print(names)

with open("..\data\json\streams_list.json", "w", encoding="utf-8") as f:
    json.dump(names, f, indent=4)

# import arcpy
# import pandas as pd

# # Set workspace
# feature_class = r"D:\path\to\your\geodatabase.gdb\your_feature_class"

# # Get field names
# fields = [field.name for field in arcpy.ListFields(feature_class)]

# # Read attributes into a DataFrame
# data = []
# with arcpy.da.SearchCursor(feature_class, fields) as cursor:
#     for row in cursor:
#         data.append(row)

# df = pd.DataFrame(data, columns=fields)
# print(df.head())  # Display the first few rows
