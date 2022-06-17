#converting then avane data set into a readable corpora
f = open("temp.txt", 'w') 
with open("avane.gn", 'r') as file:
    for line in file:
        grade_data = line.replace('\n', '')
        f.write(grade_data)
    f.close()
    file.close()

f = open("avane.gn", 'w')  
with open("temp.txt", 'r') as file:
    for line in file:
        grade_data = line.replace('.', '.\n')
        f.write(grade_data)
    f.close()
    file.close()
