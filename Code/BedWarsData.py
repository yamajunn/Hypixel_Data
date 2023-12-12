from BedWarsStatus import bedwars_status
from Who import who
import sqlite3
import csv

path = r"/Users/chinq500/Library/Application Support/minecraft/versions/1.8.9/logs/latest.log"
# path = r"C:/Users/Owner/AppData/Roaming/.minecraft/logs/blclient/minecraft/latest.log"
write_list = [i for i in range(41)]

with open(path) as f:
    s = f.read()

who_list = who(s)

data_list = []
for item in who_list:
    data_list.append(bedwars_status(item))

with open('./PlayData.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(write_list)

with open('./PlayData.csv') as f:
    print(f.read())