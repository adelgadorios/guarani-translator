#adding sentences from avane into newcorpora
with  open("avane.es","r") as f1, open("avane.gn","r") as f2, open("avane-itahari.es","w") as te, open("avane-itahari.gn","w") as tg:
    for line_es, line_gn in zip(f1, f2):
            #line_gn = list(line_gn)
            line_gn = line_gn.replace('.', '.\n')
            #line_es = list(line_es)
            line_es = line_es.replace('.', '.\n')
            te.write(line_es)
            tg.write(line_gn)
    f1.close()
    f2.close()
    te.close()
    tg.close()

#adding sentences from itahari into newcorpora
with  open("itahari.es","r") as f1, open("itahari.gn","r") as f2, open("avane-itahari.es","a") as te, open("avane-itahari.gn","a") as tg:
    for line_es, line_gn in zip(f1, f2):
            te.write(line_es)
            tg.write(line_gn)
    f1.close()
    f2.close()
    te.close()
    tg.close()


