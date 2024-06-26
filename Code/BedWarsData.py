from BedWarsStatus import bedwars_status
from Who import who
import csv
import datetime

# path = r"C:/Users/Owner/AppData/Roaming/.minecraft/logs/blclient/minecraft/latest.log"
write_list = [i for i in range(49)]

with open(path) as f:
    s = f.read()

who_list = who(s)

game_id = 0
start_data_list = []

with open('./PlayerStatus.csv') as f:  # Gameが何番目のものかを取得
    for item in csv.reader(f):
        if item[0] != "GameID":
            game_id = int(item[0])+1
        else:
            game_id = 0

with open('./PlayerStatus.csv', 'a', newline="") as f:  # Game内のプレイヤーのステータスを保存
    writer = csv.writer(f)
    for name in who_list:
        data = bedwars_status(name)
        start_data_list.append(data)
        if data[0] != True:
            data.insert(0,game_id)
            writer.writerow(data)
        else:
            data = [game_id, data[1]]
            writer.writerow(data)

y_n_input = input("データ照合 y/n")

if y_n_input == "y":
    end_data_list = []
    with open("./PlayData.csv", 'a', newline=""):
        writer = csv.writer(f)
        for name in who_list:
            end_data_list.append(bedwars_status(name))
        print(end_data_list)
