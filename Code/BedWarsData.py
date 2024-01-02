from BedWarsStatus import bedwars_status
from Who import who
import csv
import datetime

path = r"/Users/chinq500/Library/Application Support/minecraft/versions/1.8.9/logs/latest.log"
# path = r"C:/Users/Owner/AppData/Roaming/.minecraft/logs/blclient/minecraft/latest.log"
write_list = [i for i in range(49)]

with open(path) as f:
    s = f.read()

who_list = who(s)

data_list = []
# who_list = ["Gokiton"]
dt_now = datetime.datetime.now()
with open('./PlayerStatus.csv', 'a', newline="") as f:
    writer = csv.writer(f)
    for item in who_list:
        data = bedwars_status(item)
        if data[0] != True:
            data.insert(0,dt_now)
            writer.writerow(data)
        else:
            data = [dt_now, data[1]]
            writer.writerow(data)

# play_data_list = [dt_now, ]
# with open('./PlayData.csv', 'a') as f:
#     writer = csv.writer(f)
