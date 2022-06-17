c1 = "{"
c2 = "}\n"
with open("train.es", "r") as f1, open("train.gn", "r") as f2, open("guarani_corpora.json", "w") as f3: 
    for line_es, line_gn in zip(f1, f2):
        line_es = line_es.rstrip('\n')
        line_es = line_es.replace('“',"'")
        line_es = line_es.replace('"',"'")
        line_es = line_es.replace('”','')
        line_gn = line_gn.rstrip('\n')
        line_gn = line_gn.replace('“',"'")
        line_gn = line_gn.replace('"',"'")
        line_gn = line_gn.replace('”','')
        raw_data = f'{c1}"prompt": "{line_es}", "completion": "{line_gn}"{c2}'
        f3.write(raw_data)
    f1.close()
    f2.close()
    f3.close()
with open("dev.es", "r") as f1, open("dev.gn", "r") as f2, open("guarani_corpora.json", "a") as f3:
    for line_es, line_gn in zip(f1, f2):
        line_gn = line_gn.rstrip('\n')
        line_es = line_es.rstrip('\n')
        line_es = line_es.replace('"',"'")
        line_gn = line_gn.replace('"',"'")
        raw_data = f'{c1}"prompt": "{line_es}", "completion": "{line_gn}"{c2}'
        f3.write(raw_data)
    f1.close()
    f2.close()
    f3.close()

