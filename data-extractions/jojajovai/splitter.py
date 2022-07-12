import pandas as pd
# importing module from pandas import * reading CSV file
df = pd.read_csv("jojajovai_all.csv",  index_col=0)
train_gn = df.filter(regex='train', axis="index").filter(['gn'])
train_gn = train_gn['gn'].tolist()
train_es = df.filter(regex='train', axis="index").filter(['es'])
train_es = train_es['es'].tolist()

dev_gn = df.filter(regex='dev', axis="index").filter(['gn'])
dev_gn = dev_gn['gn'].tolist()
dev_es = df.filter(regex='dev', axis="index").filter(['es'])
dev_es = dev_es['es'].tolist()


test_gn = df.filter(regex='test', axis="index").filter(['gn'])
test_gn = test_gn['gn'].tolist();
test_es = df.filter(regex='test', axis="index").filter(['es'])
test_es = test_es['es'].tolist();
#splitting spanish data into a 70% train, 15% dev, and 15% test sets 
with open('train.es', 'w') as tr, open('dev.es', 'w') as dv, open('test.es','w') as test:
    for line in train_es:
        line_es = line.replace('\n', '')
        line_es = " ".join(line_es.split())
        tr.write(line_es + '\n')
    for line in dev_es:
        line_es = line.replace('\n', '')
        line_es = " ".join(line_es.split())
        dv.write(line_es + '\n')
    for line in test_es:
        line_es = line.replace('\n', '')
        line_es = " ".join(line_es.split())
        test.write(line_es + '\n')
    tr.close()
    dv.close()
    test.close()
with open('train.gn', 'w') as tr, open('dev.gn', 'w') as dv, open('test.gn','w') as test:
    for line in train_gn:
        line_gn = line.replace('\n', '')
        line_gn = " ".join(line_gn.split())
        tr.write(line_gn + '\n')
    for line in dev_gn:
        line_gn = line.replace('\n', '')
        line_gn = " ".join(line_gn.split())
        dv.write(line_gn + '\n')
    for line in test_gn:
        line_gn = line.replace('\n', '')
        line_gn = " ".join(line_gn.split())
        test.write(line_gn + '\n')
       
    tr.close()
    dv.close()
    test.close()

