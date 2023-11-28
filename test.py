
from datetime import datetime


offset = 946684800

# print(time.utime.gmtime(1701066600 - offset))

ts = 1701056023

print(datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S'))