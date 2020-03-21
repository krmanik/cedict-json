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

# To get meaning of any term from cedict-json data
1.
```
https://cdn.jsdelivr.net/gh/infinyte7/cedict-json/data/我.json
```
Fetched data
```
{
    "definitions": [
        "I",
        "my"
    ],
    "pinyin": "wo3",
    "simplified": "我",
    "traditional": "我"
}
```
2.
```
https://cdn.jsdelivr.net/gh/infinyte7/cedict-json/data/知道.json
```
Fetched data
```
{
    "definitions": [
        "to know",
        "also pr. [zhi1 dao5]"
    ],
    "pinyin": "zhi1 dao4",
    "simplified": "知道",
    "traditional": "知道"
}
```

# License
<br>cedict chinese dictionary
<br>Creative Commons Attribution-Share Alike 3.0 License
<br>https://cc-cedict.org/wiki/
