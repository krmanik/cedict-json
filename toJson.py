import os.path
import json
import ast

def get_meaning(char):
    with open("cedict_ts.u8", "r", encoding="utf-8") as f:
        lines = f.readlines()
        data = []
        pinyin = []
        meaning_dict = {}
        ch_sim = ""
        ch_trad = ""
        ch_mean = ""
        ch_pin = ""

        for line in lines:
            data = line.split(" ")
            meaning = line.split("/")
            if data[1] == char:
                ch_sim = data[1]
                ch_trad = data[0]

                source=line.strip()
                start_sep='['
                end_sep=']'
                result=[]
                tmp=source.split(start_sep)
                for par in tmp:
                    if end_sep in par:
                        result.append(par.split(end_sep)[0])

                #print(result[0])

                p = '"'+result[0]+'"'

                m = ""

                for i in range(len(meaning)):
                    if i == 0 or i == len(meaning) - 1:
                        continue
                    else:
                        m += meaning[i] + '; '

                ch_mean +=  p + ': "' + m.replace('"', "'") + '",'

                ch_pin += p + ","

            
        sim = '"simplified":' + '"' + ch_sim + '"'
        trad = '"traditional":' + '"' + ch_trad + '"'
        pin = '"pinyin":[' + ch_pin.rstrip(",") + "]"
        mean = '"definitions": {' +  ch_mean.rstrip(",") + "}"

        data = "{" + sim + "," + trad + "," + pin + "," + mean + "}"

        out = open("json/" + char + ".json", "w", encoding="utf-8")
        #out.write(data)
        data_o = ast.literal_eval(data)
        j = json.dump(data_o, out, indent=4, ensure_ascii=False)
        #print(data)       
    
# char = "的"
# get_meaning(char)

with open("list.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        char = line.strip()
        get_meaning(char)

# out = open("list.txt", "w", encoding="utf-8")

def get_first_column():
    with open("cedict_ts.u8", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            data = line.split(" ")
            #print(data[1])    
            out.write(data[1]+"\n")

# get_first_column()
