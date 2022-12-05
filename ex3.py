import datetime
import time
now = datetime.datetime.now()

format = "%H/%M"


data = datetime.datetime.now().strftime("%H%M")


print(data[0]+data[1])
print(data[2]+data[3])
#print(datetime.strptime(hour_minute, format))