primer = input('Введите выражение: ')
for i in primer: #проверяем всю строку на пробелы
    if i == ' ': 
        primer = primer[:primer.index(i)] + primer[primer.index(i)+1:] #вырезаем каждый пробел

znaki = ['+', '-', '*', '/', '^'] #дабаляем знаки действий
not_prior_znaki = ['+', '-']
prior_znaki = ['*', '/', '^']
primer = list(primer) #переводим нашу строку в список
primer1 = primer.copy() #копируем наш список
tabs = [] #тут будут храниться индексы, на которых стоят знаки
posled = [] #указываем последовательность выполнения действий
k = 0 
flag = False

for i in primer1:
    if i in znaki: #если элемент в знаках
        if i == '-' and primer1.index(i) == 0: #игнорируем первый минус, чтобы его не заносили в tabs
            k += 1
            primer1.remove(i)
        else:
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

for i in primer:
    if i in prior_znaki: #для начала добавим индексы приоритетных знаков
        if len(posled) == 0: #если список пустой
            posled.append(primer.index(i)) #то добавляем 

        else:
            for l in posled: #перебираем элементы в списке

                if primer[l] in not_prior_znaki: #если там есть знак + или - 
                    posled.insert(posled.index(l), primer.index(i)) #то добавляем приоритетный знак перед ним
                    flag = True #флаг, чтобы понять, что мы уже вставили индекс
                    break # и выходим из цикла

            if flag is False:
                posled.append(primer.index(i)) #если такого знака нету, то добавляем на последнее место

    if i in not_prior_znaki:
        if len(posled) == 0: #если список пустой
            posled.append(primer.index(i)) #то добавляем на перове место

        else:
            posled.append(primer.index(i))

    flag = False #возвращаем его в прошлое значение

def sum(b: list, a: int) -> list: #создаем функцию
    res = (float(b[a-1]) + float(b[a+1])) #и делаем первое действие
    if len(b) > 3: #если длина списка позволяет
        b.pop(a+1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        b.pop(a) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        b.pop(a-1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
    else:
        b.clear() #если не позволяет, то очищаем этот список
    b.insert(a-1, res) #и на преове место вставляем наш результат
    return b #и возвращаем наш список

def razn(b: list, a: int) -> list:
    res = (float(b[a-1]) - float(b[a+1])) #и делаем первое действие
    if len(b) > 3: #если длина списка позволяет
        b.pop(a+1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        b.pop(a) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        b.pop(a-1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
    else:
        b.clear() #если не позволяет, то очищаем этот список
    b.insert(a-1, res) #и на преове место вставляем наш результат
    return b #и возвращаем наш список

def proisv(b: list, a: int) -> list:
    res = (float(b[a-1]) * float(b[a+1])) #и делаем первое действие
    if len(b) > 3: #если длина списка позволяет
        b.pop(a+1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        b.pop(a) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        b.pop(a-1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
    else:
        b.clear() #если не позволяет, то очищаем этот список
    b.insert(a-1, res) #и на преове место вставляем наш результат
    return b #и возвращаем наш список

def chast(b: list, a: int) -> list:
    res = (float(b[a-1]) / float(b[a+1])) #и делаем первое действие
    if len(b) > 3: #если длина списка позволяет
        b.pop(a+1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        b.pop(a) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        b.pop(a-1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
    else:
        b.clear() #если не позволяет, то очищаем этот список
    b.insert(a-1, res) #и на преове место вставляем наш результат
    return b #и возвращаем наш список

def stepen(b: list, a: int) -> list:
    res = (float(b[a-1]) ** float(b[a+1])) #и делаем первое действие
    if len(b) > 3: #если длина списка позволяет
        b.pop(a+1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        b.pop(a) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        b.pop(a-1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
    else:
        b.clear() #если не позволяет, то очищаем этот список
    b.insert(a-1, res) #и на преове место вставляем наш результат
    return b #и возвращаем наш список

for i in posled:
    znak = primer[i]
    for l in primer:
        if l == znak: #перебираем знаки приеритета в элементах списка
            ind = i

            if znak == '+':
                primer = sum(primer, ind) #присваеваем то, что нам возвращает функция, чтобы использовать это заново
            elif znak == '-':
                primer = razn(primer, ind)
            elif znak == '*':
                primer = proisv(primer, ind)
            elif znak == '/':
                primer = chast(primer, ind)
            elif znak == '^':
                primer = stepen(primer, ind)

print(float(primer[0])) #берем единственный элемент нашего списка и выводим его 