import os, sys
import json

# dir = "data"
dir = "v2"

out = open("all_cedict.json", "w", encoding="utf-8")

out.write("{")
print("{")
for fn in os.listdir(dir):
    with open(dir + '/'  + fn, 'r', encoding="utf-8") as f:
        read_data = f.read()
        json_data = json.loads(read_data)
        sim = json_data["simplified"]
        data = '"' + sim + '":' + read_data
        out.write(data)
        print(data)
    out.write(",\n")
    print(",")
out.write("}")
print("}")
