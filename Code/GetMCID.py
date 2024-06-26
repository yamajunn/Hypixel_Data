import time
import copy
import csv

from BedWarsStatus import bedwars_status

def who(s):
    l = s.split("\n")
    who_list = []
    for item in l:
        if "がロビーに滑ってきました！" in item:
            # who_list = item[48:].split(", ")
            item = item[42:]
            for count, i in enumerate(item):
                if i == "]":
                    item = item[count+2:]
                    break
            for count, i in enumerate(item):
                if i == " ":
                    who_list.append(item[:count-2])
                    break
    return who_list

# path = r"C:/Users/Owner/AppData/Roaming/.minecraft/logs/blclient/minecraft/latest.log"

f = open(path)

while True:
    s = f.read()

    who_list = who(s)
    data_list = []

    for item in who_list:
        data = bedwars_status(item)
        print(data)
        if data[0] != True:
            data_list.append(data)

    if len(data_list) != 0:
        with open('./Player.csv', 'a', newline="") as e:
            writer = csv.writer(e)
            for item in data_list:
                writer.writerow(item)
    data_list = []
    time.sleep(10)
