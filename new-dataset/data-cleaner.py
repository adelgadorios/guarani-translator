#converting the spanish constitution into a readable corpora
f = open('constitution-es-separated.txt', 'w')
with open("test.txt", 'r') as file:
    for line in file:
        line = list(line)
        if(line[0].isdigit()):
            line[1] = "-"
        line = "".join(line)
        grade_data = line.replace('.', '.\n')
        f.write(grade_data)
    f.close()
# converting the guarani constitution into a readable corpora
f = open('constitution-gn-separated.txt', 'w')
with open("constitution-gn.txt", 'r') as file:
    for line in file:
        line = list(line)
        if(line[0].isdigit() and line[1].isdigit() and line[2] == ' '):
            continue
        line = "".join(line)
        grade_data = line.replace('.', '.\n')
        f.write(grade_data)
    f.close()
