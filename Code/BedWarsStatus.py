import requests
from pprint import pprint
def bedwars_status(name):
    API_KEY = "253c7c06-d1fb-49b5-99e4-3c74cbb874f5"
    try:
        def getuuid(call):
            r = requests.get(call,timeout=10)
            return r.json()

        def getinfo(call):
            r = requests.get(call,timeout=10)
            return r.json()

        name_link = f"https://api.mojang.com/users/profiles/minecraft/{name}"
        uuid = getuuid(name_link)["id"]
        uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"

        data_dic = getinfo(uuid_link)
        data_list = []
        if data_dic["success"] == True:
            if data_dic["player"] != None:
                dic_list = ['wins_bedwars', 
                            'losses_bedwars', 
                            'final_kills_bedwars', 
                            'final_deaths_bedwars', 
                            'kills_bedwars', 
                            'deaths_bedwars', 
                            'beds_broken_bedwars' , 
                            'beds_lost_bedwars',
                            'iron_resources_collected_bedwars',
                            'gold_resources_collected_bedwars',
                            'diamond_resources_collected_bedwars',
                            'emerald_resources_collected_bedwars',
                            'winstreak'
                            ]
                
                data_list.append(name)
                data_list.append(data_dic["player"]["_id"])
                data_list.append(data_dic["player"]['achievements']['bedwars_level'])
                for item in dic_list:
                    data_list.append(data_dic["player"]["stats"]["Bedwars"][item])
                data_list.append(round(data_list[3]/data_list[4], 2))
                data_list.append(round(data_list[5]/data_list[6], 2))
                data_list.append(round(data_list[7]/data_list[8], 2))
                data_list.append(round(data_list[9]/data_list[10], 2))
                return data_list
            else:
                return [True, name]
        else:
            return [True, name]
    except KeyError:
        return [True, name]
# bedwars_status("Gokiton")