import os
import json
from shutil import copyfile

from hanziconv import HanziConv
from googletrans import Translator
import subprocess

import colorize_pinyin

from random import randint
from time import sleep

def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


def copy_from_v2_to_HSK(fname):
    import pinyin_jyutping_sentence

    path = "HSK Meaning/" + fname

    # Write output as tsv file Simplified, Traditional, Pinyin, Audio and Meaning
    out = open(path + ".txt", "w", encoding="utf-8")

    # Some HSK words are not listed in CC-EDICT
    not_found = open("HSK/list/Not Found " + fname + ".txt", "w", encoding="utf-8")

    # Read HSK Simplified character list and use this list to create tsv file
    with open("HSK List/" + fname + ".txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            # print(line)

            # Get meaning from v2 folder of cedict-json
            src_fname = "v2/" + line.strip() + ".json"

            if os.path.exists(src_fname):
                with open(src_fname, "r", encoding="utf-8") as mean_f:
                    # load character json
                    jd = json.load(mean_f)

                    # print(jd)

                    simplified = jd['simplified']
                    traditional = jd['traditional']
                    definitions =  jd['definitions']

                    pinyin = []
                    mean_data = ""

                    # Create pinyin with tone color and meaning for respective pinyin
                    for de in definitions:
                        meanings = definitions[de]
                        meanings = meanings.split(";")

                        html_mean = "<div class='meaning'><ul>"
                        for me in meanings:
                            html_mean += "<li>" + me + "</li>"
                        html_mean += "</ul></div>"
                        html_mean = html_mean.replace('<li> </li>', '')

                        # Use node and pinyin_converter.js to convert number pinyin to tone marks
                        p = subprocess.Popen(["node", "index.js", de], stdout=subprocess.PIPE)
                        de, err = p.communicate()
                        de = de.decode('utf-8').strip()

                        # Colorize pinyin wrap in span html tag with tone1, tone2... class
                        colp = colorize_pinyin.colorized_HTML_string_from_string(de)

                        # Some pinyin like de with is not colorize so add tone5 class in span tag
                        if not colp:
                            # print(de)
                            # print(colp)
                            colp = '<span class="tone5">' + de + '</span>'

                        pinyin.append(colp)

                        # Create meaning with matched pinyin
                        # mean_data += "<div class='pinyin'>" + colp + "</div>" + html_mean
                        mean_data += html_mean

                        # print(definitions[d])

                    pinyin = list(unique(pinyin))
                    pinyin = ", ".join(pinyin)
                    audio = "[sound:cmn-" + simplified + ".mp3]"

                    data = simplified + "\t" + traditional + "\t" + pinyin + "\t" + audio + "\t" + mean_data + "\n"

                    out.write(data)
                    # print(data)

            # Create tsv for simplified character using Google Translate
            else:
                simplified =  line.strip()
                mean_data = ""

                # For large list use this
                # sleep(randint(1, 5))

                # translator = Translator()
                # tr = translator.translate(simplified, src='zh-cn', dest="en")
                # mean_data = tr.text 

                with open("HSK List/old/" + fname + ".tsv", "r", encoding="utf-8") as f:
                    lines =  f.readlines()
                    for line in lines:
                        split = line.split("\t")

                        if split[1] == simplified:                            
                            mean_data = split[3]

                pinyin = pinyin_jyutping_sentence.pinyin(simplified)
                traditional = HanziConv.toTraditional(simplified)

                colp = colorize_pinyin.colorized_HTML_string_from_string(pinyin)
                print(colp)

                if not colp:
                    print(pinyin)
                    colp = '<span class="tone5">' + pinyin + '</span>'

                html_mean = "<div class='meaning'><ul><li>" + mean_data + "</li></ul></div>"

                #html_mean = "<div class='pinyin'>" + colp + "</div>" + html_mean

                audio = "[sound:cmn-" + simplified + ".mp3]"

                data = simplified + "\t" + traditional + "\t" + colp + "\t" + audio + "\t" + html_mean + "\n"
                out.write(data)
                # print(data)
                not_found.write(line)            

def first(fname):
    out = open("HSK List/" + fname + " - new.txt", "w", encoding="utf-8")    
    with open("HSK List/" + fname + ".txt", "r", encoding="utf-8") as f:
        lines =  f.readlines()
        for line in lines:
            split = line.split("\t")
            ch_sim = split[0].split("[", 1)[0]
            print(ch_sim)
            ch_sim = ch_sim + "\n"
            out.write(ch_sim)

def not_in_v2():
    out = open("not_found.txt", "w", encoding="utf-8")
    with open("HSK List/HSK 7-9.txt", "r", encoding="utf-8") as f:
        lines =  f.readlines()
        for line in lines:
            char = line.strip()
            fname = "v2/" + char + ".json"
            if not os.path.exists(fname):
                out.write(line)
            
# not_in_v2()

# first("hsk7-9")

# Change HSK 1..7-9
copy_from_v2_to_HSK("HSK 7-9")

# a = call(["node", "index.js", '"yi1 hui4 r5"'])
# a  = os.popen('node index.js "yi1 hui4 r5"').readlines()
# print(a[0].encode('utf-8'))


# p = subprocess.Popen(["node", "index.js", '"yi1 hui4 r5"'], stdout=subprocess.PIPE)
# out, err = p.communicate()
# print(out.decode('utf-8'))
