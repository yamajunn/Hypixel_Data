# path = r"/Users/chinq500/Library/Application Support/minecraft/versions/1.8.9/logs/latest.log"
path = r"C:/Users/Owner/AppData/Roaming/.minecraft/logs/blclient/minecraft/latest.log"
with open(path) as f:
    s = f.read()
    l = s.split("\n")
    for item in l:
        print(item)