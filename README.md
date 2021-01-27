# cedict-json

cedict-json individual json data of dictionary term according to simplified terms.

# Quick Start
1. Fork this repository
2. Get meaning using cdn for v2 data
```
https://cdn.jsdelivr.net/gh/<your-username>/cedict-json/v2/我.json
```
Note: ```<your-username> is your GitHub username```

3. The v2 data
```json
{
    "simplified": "我",
    "traditional": "我",
    "pinyin": [
        "wo3"
    ],
    "definitions": {
        "wo3": "I; me; my; "
    }
}
```
4. Multiple meanings are separated by semi-color ```;```
e.g. three meaning for ```我```
```json
    "definitions": {
        "wo3": "I; me; my; "
    }
```

# Version 2
## Generated using [toJson.py](toJson.py) script

### Difference between version 1 (v1) and version 2 (v2)

Some words (approx. 3000) have same character and different pinyin and meaning. So using [toJson.py](toJson.py) words merged.
For e.g. ```的``` have more than one pinyin and meaning. But in version 1 there is one pinyin. So use v2 for getting meaning data.

```json
{
    "simplified": "的",
    "traditional": "的",
    "pinyin": [
        "de5",
        "di1",
        "di2",
        "di4"
    ],
    "definitions": {
        "de5": "of; ~'s (possessive particle); (used after an attribute); (used to form a nominal expression); (used at the end of a declarative sentence for emphasis); ",
        "di1": "see 的士[di1 shi4]; ",
        "di2": "really and truly; ",
        "di4": "aim; clear; "
    }
}
```
```
```
# Version 1 
### Generated using following script：
```python
with open('cedict.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    for x in range(0, 114852):
        print(data[x]['simplified'])
        name = data[x]['simplified']
        name += '.json'
        
        with open(name, "w", encoding='utf8') as f:
            json.dump(data[x],f,indent=4,sort_keys=True, ensure_ascii=False)
```
 
### cedict.json file generated using following:
https://github.com/kevb34ns/CEDICT2JSON

## To get meaning of any term from cedict-json data
Example 1
```
https://cdn.jsdelivr.net/gh/<your-username>/cedict-json/data/我.json
```
Fork this and then, <br>
your-username is your github username

Fetched data
```json
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
Example 2
```
https://cdn.jsdelivr.net/gh/infinyte7/cedict-json/data/知道.json
```
Fetched data
```json
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

## License
#### cedict chinese dictionary
Creative Commons Attribution-Share Alike 4.0 License
<br>https://cc-cedict.org/wiki/

#### cedict-json
Mani (Infinyte7)
<br>Creative Commons Attribution-Share Alike 4.0 License
