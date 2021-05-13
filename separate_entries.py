def separate_entries():
    single_entry = open("text/single_entry.txt", "w", encoding="utf-8")
    multiple_entry = open("text/multiple_entry.txt", "w", encoding="utf-8")

    with open('cedict_ts.u8', "r", encoding="utf-8") as f:
        lines = f.readlines()
        dict_data = []
        not_dict_data = []

        for line in lines:
            data = line.split(" ")
            meaning = line.split("/")
            
            if data[1] not in dict_data:
                print("Single: ", line)
                dict_data.append(data[1].strip())
                single_entry.write(line)
            else:
                not_dict_data.append(data[1].strip())
                print("Multiple: ", line)
                multiple_entry.write(line)

    single_entry.close()
    multiple_entry.close()

    
