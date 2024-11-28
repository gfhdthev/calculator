primer = input('Введиле выражение с 2 цифрами: ')
for i in primer:
    if i == ' ':
        primer = primer[:primer.index(i)] + primer[primer.index(i)+1:]

znaki = ['+', '-', '*', '/']
primer = list(primer)
oper = 0
flag = False
opers = []

for i in primer:
    if i in znaki:
        oper += 1

'''
for i in primer:
    if flag == True:
        primer.insert(primer.index(i)-1, ' ')
        primer.insert(primer.index(i), ' ')
        flag = False
    if i in znaki:
        flag = True
        continue
'''


primer = ''.join(primer)

for i in primer:
    if i in znaki:
        primer = primer.split(i)
        opers.append(i)

print(opers)
print(primer)

'''
def sum(b):
    res = (int(b[0]) + int(b[2]))
    primer = primer[3:]
    primer = (res + primer)
    return primer
def razn(b):
    return(int(b[0]) - int(b[2]))
def proisv(b):
    return(int(b[0]) * int(b[2]))
def chast(b):
    return(int(b[0]) / int(b[2]))

for i in range(oper):
    if primer[1] == '+':
        sum(primer)
    if primer[1] == '-':
        razn(primer)
    if primer[1] == '*':
        proisv(primer)
    if primer[1] == '/':
        chast(primer)
'''
