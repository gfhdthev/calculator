primer = input('Введиле выражение с 2 цифрами: ')
for i in primer:
    if i == ' ':
        primer = primer[:primer.index(i)] + primer[primer.index(i)+1:]

znaki = ['+', '-', '*', '/']
primer1 = list(primer).copy()
primer = list(primer)
oper = 0
tabs = []
l = 0
k = 0

for i in primer1:
    if i in znaki:
        tabs.append(primer1.index(i)+k)
        oper += 1
        k += 1
        primer1.remove(i)

for i in tabs:
    primer.insert(i+l+1, ' ')
    primer.insert(i+l, ' ')
    l += 2

primer = ''.join(primer)
primer = primer.split()

def sum(b: list) -> list:
    res = (int(b[0]) + int(b[2]))
    if len(b) >3:
        b = b[3:]
        print(b)
    else:
        b.clear()
    b.insert(0, res)
    list = b.copy()
    return list

def razn(b: list) -> list:
    res = (int(b[0]) - int(b[2]))
    if len(b) >3:
        b = b[3:]
    else:
        b.clear()
    b.insert(0, res)
    return b

def proisv(b: list) -> list:
    res = (int(b[0]) * int(b[2]))
    if len(b) >3:
        b = b[3:]
    else:
        b.clear()
    b.insert(0, res)
    return b

def chast(b: list) -> list:
    res = (int(b[0]) / int(b[2]))
    if len(b) >3:
        b = b[3:]
    else:
        b.clear()
    b.insert(0, res)
    return b

for i in range(oper):
    if primer[1] == '+':
        sum(primer)
    elif primer[1] == '-':
        razn(primer)
    elif primer[1] == '*':
        proisv(primer)
    elif primer[1] == '/':
        chast(primer)

print(primer)