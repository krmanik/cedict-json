import os.path
import json
import ast
from shutil import copyfile

# https://stackoverflow.com/questions/54357405/combine-duplicate-keys-in-json
def myhook(pairs):
    d = {}
    for k, v in pairs:
        if k not in d:
          d[k] = v
        else:
          d[k] += v
    return d

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
        # out.write(data)
        # data_o = ast.literal_eval(data)
        jd = json.loads(data, object_pairs_hook=myhook)
        jd['pinyin'] = list(set(jd['pinyin']))
        j = json.dump(jd, out, indent=4, ensure_ascii=False)
        print(jd)

def get_first_column():
    out = open("list.txt", "w", encoding="utf-8")
    out_found = open("list_found.txt", "w", encoding="utf-8")
    with open("cedict_ts.u8", "r", encoding="utf-8") as f:
        lines = f.readlines()
        line_data = []
        found = []
        for line in lines:
            data = line.split(" ")
            #print(data[1])
            if data[1] not in line_data:
                line_data.append(data[1])
            else:
                found.append(data[1])
        
        line_data = "\n".join(line_data)
        found = "\n".join(found)

        out.write(line_data)
        out_found.write(found)

def copy_dups_to_v3():
    with open("list_found_dup.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            src_filename = "v2/" + line.strip() + ".json"
            dest_filename = "v3/" + line.strip() + ".json"
            copyfile(src_filename, dest_filename)

            print(line)


def toJson():
    with open("list_found_dup.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            char = line.strip()
            get_meaning(char)

# get_first_column()

# char = "的"
# char = "和"
# get_meaning(char)

# toJson()

# copy_dups_to_v3()