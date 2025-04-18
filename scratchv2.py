from datetime import datetime

date = "July, 27 2020 00:00:00"
print(datetime.strptime(date, "%B, %d %Y %H:%M:%S"))
