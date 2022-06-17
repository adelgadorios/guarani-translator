class Solution:
   def solve(self, s0, s1):
      s0 = s0.lower()
      s1 = s1.lower()
      s0List = s0.split(" ")
      s1List = s1.split(" ")
      return len(list(set(s0List)&set(s1List)))
ob = Solution()

#cleaning train files from jopara
with  open("backup/train.es","r") as f1, open("backup/train.gn","r") as f2, open("train.es","w") as te, open("train.gn","w") as tg:
    for line_es, line_gn in zip(f1, f2):
            common = ob.solve(line_gn,line_es)
            if(common >2):
                continue
            te.write(line_es)
            tg.write(line_gn)
    f1.close()
    f2.close()
    te.close()
    tg.close()

#cleaning dev files from jopara
with  open("backup/dev.es","r") as f1, open("backup/dev.gn","r") as f2, open("dev.es","w") as te, open("dev.gn","w") as tg:
    for line_es, line_gn in zip(f1, f2):
            common = ob.solve(line_gn,line_es)
            if(common >2):
                continue
            te.write(line_es)
            tg.write(line_gn)
    f1.close()
    f2.close()
    te.close()
    tg.close()
#cleaning test files from jopara
with  open("backup/test.es","r") as f1, open("backup/test.gn","r") as f2, open("test.es","w") as te, open("test.gn","w") as tg:
    for line_es, line_gn in zip(f1, f2):
            common = ob.solve(line_gn,line_es)
            if(common >2):
                continue
            te.write(line_es)
            tg.write(line_gn)
    f1.close()
    f2.close()
    te.close()
    tg.close()
