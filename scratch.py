import pandas as pd

import json
import pandas as pd
import openpyxl

# Load the JSON file
with open(r"data\json\combinedV2.json") as f:
    data = json.load(f)

rivers = []
for i in data["DATA"]:
    if i[7] not in rivers:
        rivers.append(i[7])

print(rivers)
