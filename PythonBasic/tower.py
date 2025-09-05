file = open('note.config',"r")
for lines in file:
    line = lines.strip()
    if 'x' in line:
        a = line.split('x',1)
        num = int(a[0])
        sing = a[1]
    for _ in range(num):
        print(sing)


