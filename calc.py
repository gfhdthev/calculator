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
k = 0 

'''ФУНКЦИИ'''

def prior(b: list, posl: list) -> list:
    flag = False

    for i in b:
        if i in prior_znaki: #для начала добавим индексы приоритетных знаков
            if len(posl) == 0: #если список пустой
                posl.append(b.index(i)) #то добавляем 
            else:
                for l in posl: #перебираем элементы в списке
                    if b[l] in not_prior_znaki: #если там есть знак + или - 
                        posl.insert(posl.index(l), b.index(i)) #то добавляем приоритетный знак перед ним
                        flag = True #флаг, чтобы понять, что мы уже вставили индекс
                        break # и выходим из цикла

                if flag is False:
                    posl.append(b.index(i)) #если такого знака нету, то добавляем на последнее место

        if i in not_prior_znaki:
            if len(posl) == 0: #если список пустой
                posl.append(b.index(i)) #то добавляем на перове место

            else:
                posl.append(b.index(i))

        flag = False #возвращаем его в прошлое значение

    return posl

def del_skob(b: list) -> list:
    posled_skob = [] #тут будут храниться действия в скобках
    k = -1
    n = 0

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

    b.pop(ind_f) #удаляем скобки
    b.pop(ind_s)

    posl = prior(line, posled_skob)

    for i in posl:
        i += ind_s #добавляем индекс начала скобок, чтобы компенсировать то, что мы брали скобку

    return b


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

'''РАССТАВЛЯЕМ ПРИОРИТЕТ СКОБОК'''
'''
while '(' in primer:
    k = -1 #устанавливаем k
    n = 0
    
    for i in primer:
        if i == '(':
            if k == -1: #проверяем, чтобы это была первая скобка
                ind_s = primer.index(i) #берем начало скобки
                k += 1 #k нам нужна, чтобы знать, сколько скобок пропустить, до закрытия нужной. Для этого мы и ставили -1,
                #чтобы не пропускать скобку, если она одна
            else:
                k += 1 #если это не первая скобка, то просто добавляем значение, чтобы ее пропустить

        elif i == ')':
            if k == 0: #проверяем, чтобы эта была именно та скобка, которая закрывает нужную
                ind_f = primer.index(i) #берем конец скобки
            else:
                k -= 1

    line = primer[ind_s+1:ind_f] #берем следующий от пеовй скобки индекс

    for i in line:
        if i not in znaki:
            n += 1 #смотрим, сколько элементов в выбранной скобке

    if n > 1:
        primer.pop(ind_f) #удаляем скобки
        primer.pop(ind_s) 

        posled_skob = prior(line, posled_skob) #получаем последовательность действи  в скобках

    else:
        primer.pop(ind_f) #удаляем скобки
        primer.pop(ind_s) 
'''
while '(' in primer:
    primer = del_skob(primer)


primer1 = primer.copy() #копируем ввод уже без скобок

for i in posled_skob:
    primer1.insert(i, '!') #и заменяем те знаки, которые мы уже занесли в последовательность на !
    primer1.pop(i+1) #чтобы не заносить их дважды
print(primer1)
'''РАССТАВЛЯЕМ ПРИОРИТЕТ ЗНАКОВ'''

posled = prior(primer1, posled) #создаем общую последовательность из индексов
print(posled_skob)
print(posled)
posled_ob = posled_skob + posled #объединяем и получаем общую последовательность

'''СЧИТАЕМ РЕЗУЛЬТАТ'''
print(primer)
print(posled_ob)
for i in posled_ob:
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