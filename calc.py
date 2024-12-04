primer = input('Введите выражение: ')

for i in primer: #проверяем всю строку на пробелы
    if i == ' ': 
        primer = primer[:primer.index(i)] + primer[primer.index(i)+1:] #вырезаем каждый пробел

'''ПЕРЕМЕННЫЕ'''

znaki = ['+', '-', '*', '/', '^', '(', ')'] #добаляем знаки действий
not_prior_znaki = ['+', '-']
prior_znaki = ['*', '/', '^']
primer = list(primer) #переводим нашу строку в список
tabs = [] #тут будут храниться индексы, на которых стоят знаки
posled = [] #указываем последовательность выполнения действий не в скобках
posled_skob = [] #тут будут храниться действия в скобках
posled_ob = []
posl = []
k = 0 


'''ФУНКЦИИ'''

def prior(b: list, posl: list) -> list:
    flag = False

    for i in b:
        ind = b.index(i)
        if i in prior_znaki: #для начала добавим индексы приоритетных знаков
            if len(posl) == 0: #если список пустой
                posl.append(b.index(i)) #то добавляем 
                #b.insert(ind, '!')
                #b.pop(ind+1)

            else:
                for l in posl: #перебираем элементы в списке
                    if b[l] in not_prior_znaki: #если там есть знак + или - 
                        posl.insert(posl.index(l), b.index(i)) #то добавляем приоритетный знак перед ним
                        #b.insert(ind, '!')
                        #b.pop(ind + 1)

                        flag = True #флаг, чтобы понять, что мы уже вставили индекс
                        break # и выходим из цикла

                if flag is False:
                    posl.append(b.index(i)) #если такого знака нету, то добавляем на последнее место
                    #b.insert(ind, '!')
                    #b.pop(ind + 1)


        if i in not_prior_znaki:
                posl.append(b.index(i))
                #b.insert(ind, '!')
                #b.pop(ind + 1)


        flag = False #возвращаем его в прошлое значение

    return posl


def del_skob(b: list) -> list:
    k = -1

    for i in b:
        if i == '(': #ищем начало скобки
            if k  == -1: #и если это скобка первая, то мы берем ее индекс
                ind_s = b.index(i)
                k += 1
            else:
                k += 1 #если не первая, то указываем, сколько закрывающихся скобок надо пропустить

        if i == ')':
            if k == 0: #если надо пропустить 0, то берем индекс первой же закрытой скобки
                ind_f = b.index(i)
            else:
                k -= 1

    b.pop(ind_f) #удаляем скобки
    b.pop(ind_s)

    return b #возвращаем пример без скобок

def posl_skob(b: list) -> list:
    posled_skob = [] #тут будут храниться действия в скобках
    n = 0
    k = -1

    for i in b:

        if i == '(':
            if k  == -1:
                ind_s = b.index(i)

                k += 1
            else:
                k += 1
        if i == ')':
            if k == 0:
                ind_f = b.index(i)
            else:
                k -= 1

    line = b[ind_s+1:ind_f] #составляем выражение внутри скобок

    for i in line:
        if i not in znaki:
            n += 1 #смотрим, сколько чисел внутри скобок

    if n == 1:
        return posled_skob #если одно число(например -7), то просто возвращаем пустой список

    else:
        posled_skob = prior(line, posled_skob) #расставляем приоритет

        for i in range(len(posled_skob)):
            posled_skob[i] += ind_s #добавляем индекс начала скобок, чтобы компенсировать то, что мы брали не весь пример, а только его часть
        return posled_skob


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

'''РАЗДЕЛЯЕМ ЧИСЛА И ЗНАКИ ПРОБЕЛАМИ'''

while '(' in primer:
    posled_ob.append(posl_skob(primer))
    primer = del_skob(primer)

for i in range(len(primer)):
    if primer[i] in znaki: #если элемент в знаках
        if primer[i] == '-' and i == 0: #игнорируем первый минус, чтобы его не заносили в tabs
            continue
        else:
            tabs.append(i) #то мы добавляем его индекс

for i in range(len(tabs)): #перебираем индексы, на которых стоят знаки
    if tabs[i] - tabs[i-1] == 1: #если знаки идут подряд
        if primer[tabs[i] + k] == '-': #и второй знак это минус
            tabs.pop(i) #то мы просто удаляем его индекс из списка

        else:
            primer.insert(tabs[i]+k+1, ' ') #если не минус, то добавляем пробелы
            primer.insert(tabs[i]+k, ' ')
    else:
        primer.insert(tabs[i]+k+1, ' ') #если не идут подряд, то добавляем пробелы
        primer.insert(tabs[i]+k, ' ')
    k += 2 #l нам нужны, потому что, когда мы добавляем 2 пробела, то наш список увеличивается на 2

primer = ''.join(primer) #переаводим все в строку
primer = primer.split() #и иразделяем эту строку на числа и знаки

'''РАССТАВЛЯЕМ ПРИОРИТЕТ'''
    
for i in posled_ob: #из функции мы получаем список списков 
    for l in i:
        posl.append(l) #добавляем ВСЕ элементы в один список

primer1 = primer.copy()

for i in posl:
    primer1.insert(i, '!') #и заменяем те знаки, которые мы уже занесли в последовательность на !
    primer1.pop(i+1) #чтобы не заносить их дважды

posled = prior(primer1, posled) #создаем общую последовательность из индексов
posl += posled #объединяем и получаем общую последовательность


for i in range(len(posl)): #проходим по всем элементам
    n = 1
    for l in range(len(posl)-i-1): #тут убираем элементы, которые уже прошли или проходят внешний цикл
        if posl[i] < posl[i+n]: #и если индекс меньше, последующих, то для него операция будет раньше и он сместит все интексы на 2
            posl[i+n] -= 2 #мы убираем эти 2 
        n += 1

for i in posl:
    znak = primer[i] #смотрим, с каким знаком сейчас должна быть операция
    for l in primer:

        if l == znak: #перебираем знаки приеритета в элементах списка
            ind = i

            if znak == '+':
                primer = sum(primer, ind) #присваеваем то, что нам возвращает функция, чтобы использовать это заново
            if znak == '-':
                primer = razn(primer, ind)
            if znak == '*':
                primer = proisv(primer, ind)
            if znak == '/':
                primer = chast(primer, ind)
            if znak == '^':
                primer = stepen(primer, ind)
            break

print(float(primer[0])) #берем единственный элемент нашего списка и выводим его 