def find_common(s0, s1):
    s0 = s0.lower()
    s1 = s1.lower()
    s0List = s0.split(" ")
    s1List = s1.split(" ")
    return len(list(set(s0List) & set(s1List)))
count = 0
with open("news-data.txt", "r") as f1, open("train-uruguay.es", "w") as te, open("train-uruguay.gn", "w") as tg:
    for line in f1:
        if "gn:" in line:
            count += 1
            line_gn = line.replace('\n', '')
            line_gn = line_gn.replace("gn:", '')
            #replacing incorrect symbols(this mistake is also present on original dataset)
            line_gn = line_gn.replace('“', '"')
            line_gn = line_gn.replace('’', "'")
            line_gn = line_gn.replace('”', '"')
           """
           #scrapped for now as I need to ook at the possible effects this may have on accuracy
            line_gn = line_gn.replace('î', 'ĩ')
            line_gn = line_gn.replace('ä', 'ĩ')
            line_gn = line_gn.replace('ÿ', 'ỹ')
            line_gn = line_gn.replace('ê', 'ẽ')
            line_gn = line_gn.replace('â', 'ã')
            line_gn = line_gn.replace('ô', 'õ')
            line_gn = line_gn.replace('û', 'ũ')
           """ 
            line_gn = " ".join(line_gn.split())
            line_es = next(f1)
            line_es = " ".join(line_es.split())
            line_es = line_es.replace('“', '"')
            line_es = line_es.replace('”', '"')
            line_es = line_es.replace('\n', '')
            line_es = line_es.replace("es:", '')
            common = find_common(line_gn, line_es)
            if line_es == "Pág" or len(line_es) > 2*len(line_gn) or len(line_gn) < 40 or common > 4 or len(line_gn) > len(line_es):
                continue
            te.write(line_es + '\n')
            tg.write(line_gn + '\n')
    te.close()
    tg.close()
    f1.close()
