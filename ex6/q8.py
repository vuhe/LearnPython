import json

fr = open("./resources/学生.csv", "r")
ls = []
for line in fr:
    line = line.replace('\n', '')
    ls.append(line.split(','))
fr.close()
for i in range(1, len(ls)):
    ls[i] = dict(zip(ls[0], ls[i]))

print(json.dumps(ls[1:], indent=4, ensure_ascii=False))
