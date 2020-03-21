# cedict-json

cedict-json individual json data of dictionary term according to simplified terms.

generated using following script：
```
with open('cedict.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    for x in range(50000, 114852):
        print(data[x]['simplified'])
        name = data[x]['simplified']
        name += '.json'
        
        with open(name, "w", encoding='utf8') as f:
            json.dump(data[x],f,indent=4,sort_keys=True, ensure_ascii=False)
```
 
cedict.json file generated using following:
<br>https://github.com/kevb34ns/CEDICT2JSON


# License
<br>cedict chinese dictionary
<br>Creative Commons Attribution-Share Alike 3.0 License
<br>https://cc-cedict.org/wiki/
