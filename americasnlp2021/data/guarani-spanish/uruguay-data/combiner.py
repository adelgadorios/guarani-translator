class Solution:
    def solve(self, s0, s1):
        s0 = s0.lower()
        s1 = s1.lower()
        s0List = s0.split(" ")
        s1List = s1.split(" ")
        return len(list(set(s0List) & set(s1List)))


ob = Solution()
count = 0
with open("combined.txt", "r") as f1, open("train2.es", "w") as te, open("train2.gn", "w") as tg, open("test.es", "w") as testes, open("test.gn", "w") as testgn:
    for line in f1:
        if "gn:" in line:
            count += 1
            line_gn = line.replace('\n', '')
            line_gn = line_gn.replace("gn:", '')
            line_gn = line_gn.replace('“', "'")
            line_gn = line_gn.replace('"', "'")
            line_gn = line_gn.replace('”', '')
            line_gn = " ".join(line_gn.split())
            line_es = next(f1)
            line_es = " ".join(line_es.split())
            line_es = line_es.replace('“', "'")
            line_es = line_es.replace('"', "'")
            line_es = line_es.replace('”', '')
            line_es = line_es.replace('\n', '')
            line_es = line_es.replace("es:", '')
            common = ob.solve(line_gn, line_es)
            if line_es == "Pág" or len(line_es) > 2*len(line_gn):
                continue
            if(common > 3):
                continue
            if count > 25000:
                testes.write(line_es + '\n')
                testgn.write(line_gn + '\n')

            else:
                te.write(line_es + '\n')
                tg.write(line_gn + '\n')
    te.close()
    tg.close()
    testes.close()
    testgn.close()
    f1.close()
