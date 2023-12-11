from BedWarsStatus import bedwars_status
from Who import who

# path = "/Users/chinq500/Library/Application Support/minecraft/versions/1.8.9/logs/latest.log"
path = r"C:/Users/Owner/AppData/Roaming/.minecraft/logs/blclient/minecraft/latest.log"
with open(path) as f:
    s = f.read()

for item in who(s):
    print(bedwars_status(item))