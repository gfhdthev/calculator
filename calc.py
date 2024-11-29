primer = input('Введиле выражение: ')
for i in primer: #проверяем всю строку на пробелы
    if i == ' ': 
        primer = primer[:primer.index(i)] + primer[primer.index(i)+1:] #вырезаем каждый пробел

znaki = ['+', '-', '*', '/', '^'] #дабваляем знаки действий
primer = list(primer) #переводим нашу строку в список
primer1 = primer.copy() #копируем наш список
tabs = [] #тут будут храниться индексы, на которых стоят знаки
k = 0 

for i in primer1:
    if i in znaki: #если элемент в знаках
        tabs.append(primer1.index(i)+k) #то мы добваляем его индекс + k
        k += 1 #k нам нужна, потому что, когда мы удаляем индекс, то наш список уменьшается в длину на 1 и индексы сдвигаются
        #а с помощью k мы компенсируем эти удаления
        primer1.remove(i) #и удаляем наш знак

k = 0 #очищаем переменную

for i in tabs: #перебираем индексы, на которых стоят знаки
    primer.insert(i+k+1, ' ') #добавляем пробел после этого знака
    primer.insert(i+k, ' ') #и перед
    k += 2 #l нам нужны, потому что, когда мы добавляем 2 пробела, то наш список увеличивается на 2

primer = ''.join(primer) #переаводим все в строку
primer = primer.split() #и иразделяем эту строку на числа и знаки

def sum(b: list) -> list: #создаем функцию
    res = (float(b[0]) + float(b[2])) #и делаем первое действие
    if len(b) > 3: #если длина списка позволяет
        b = b[3:] #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
    else:
        b.clear() #если не позволяет, то очищаем этот список
    b.insert(0, res) #и на преове место вставляем наш результат
    return b #и возвращаем наш список

def razn(b: list) -> list:
    res = (float(b[0]) - float(b[2]))
    if len(b) > 3:
        b = b[3:]
    else:
        b.clear()
    b.insert(0, res)
    return b

def proisv(b: list) -> list:
    res = (float(b[0]) * float(b[2]))
    if len(b) > 3:
        b = b[3:]
    else:
        b.clear()
    b.insert(0, res)
    return b

def chast(b: list) -> list:
    res = (float(b[0]) / float(b[2]))
    if len(b) > 3:
        b = b[3:]
    else:
        b.clear()
    b.insert(0, res)
    return b

def stepen(b: list) -> list:
    res = (float(b[0]) ** float(b[2]))
    if len(b) > 3:
        b = b[3:]
    else:
        b.clear()
    b.insert(0, res)
    return b

while len(primer) != 1: #цикл будет работать, покуда в списке не останется 1 элемент (наш результат)
    if primer[1] == '+':
        primer = sum(primer) #присваеваем то, что нам возвращает функция, чтобы использовать это заново
    elif primer[1] == '-':
        primer = razn(primer)
    elif primer[1] == '*':
        primer = proisv(primer)
    elif primer[1] == '/':
        primer = chast(primer)
    elif primer[1] == '^':
        primer = stepen(primer)

print(float(primer[0])) #берем единственный элемент нашего списка и выводим его 