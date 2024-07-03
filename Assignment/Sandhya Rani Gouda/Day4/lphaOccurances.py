count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
text = "Sentance to count from"
for x in text:
    asc = ord(x)
    if (asc>=65 and asc<=90):
        count[asc-65] += 1
    elif (asc>=97 and asc<=122):
        count[asc-97] += 1

for i in range(0, len(count)):
    if(count[i]>0):
        print(chr(i+65), ' = ', count[i])