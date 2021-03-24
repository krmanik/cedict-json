import json
with open("all_cedict.json", "r", encoding="utf-8") as f:
    data = json.load(f)

#print(data["比如"])
print(data["比如"]["simplified"])
