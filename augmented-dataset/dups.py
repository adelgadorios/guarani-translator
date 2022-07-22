import sys
def unique_generator(things):
    visited = set()
    for thing in things:
        if thing in visited:
            continue
        visited.add(thing)
        yield thing

with open("train.es") as xh:
  with open('train.gn') as yh:
    with open("combined.txt","w") as zh:
      #Read first file
      xlines = xh.readlines()
      #Read second file
      ylines = yh.readlines()
      #Combine content of both lists  and Write to third file
      for line1, line2 in zip(ylines, xlines):
          line1 = line1.replace('\n', '')
          line2 = line2.replace('\n', '')
          zh.write("{}{}\n".format(line1.rstrip() + '\t', line2.rstrip()))
    xh.close()
    yh.close()
with open('deduped.txt','w') as de:
    for line in unique_generator(open("combined.txt")):
            de.write(line)
    de.close()
with open('te.es', 'w') as fe, open('tg.gn', 'w') as fg, open('deduped.txt','r') as cmb:
    for line in cmb:
            line = line.replace('\n', '')
            line = line.replace('î', 'ĩ')
            #line = line.replace('ä', 'ĩ')
            #line = line.replace('ÿ', 'ỹ')
            line = line.replace('ê', 'ẽ')
            line = line.replace('â', 'ã')
            line = line.replace('ô', 'õ')
            line = line.replace('û', 'ũ')
            line = line.split('\t')
            fg.write(line[0]+'\n')
            fe.write(line[1]+'\n')
