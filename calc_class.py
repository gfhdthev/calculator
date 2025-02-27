#gfhdthev
#Калькулятор с классом


znaki = ['+', '-', '*', '/', '^'] #дабаляем знаки действий
not_prior_znaki = ['+', '-']
prior_znaki = ['*', '/', '^']
tabs = [] #тут будут храниться индексы, на которых стоят знаки
posled = [] #указываем последовательность выполнения действий
flag = False


class Calc:

    def __init__(self, primer):
        self.primer = primer
        self.k = 0 

    def itog_primer(self):
        self.primer = list(self.primer)
        self.primer1 = self.primer.copy() #копируем наш список

        for i in self.primer: #проверяем всю строку на пробелы
            if i == ' ': 
                self.primer = self.primer[:self.primer.index(i)] + self.primer[self.primer.index(i)+1:] #вырезаем каждый пробел

        for i in self.primer1:
            if i in znaki: #если элемент в знаках
                if i == '-' and self.primer1.index(i) == 0: #игнорируем первый минус, чтобы его не заносили в tabs
                    self.k += 1
                    self.primer1.remove(i)
                else:
                    tabs.append(self.primer1.index(i)+self.k) #то мы добавляем его индекс + k
                    self.k += 1 #k нам нужна, потому что, когда мы удаляем индекс, то наш список уменьшается в длину на 1 и индексы сдвигаются
                    #а с помощью k мы компенсируем эти удаления
                    self.primer1.remove(i) #и удаляем наш знак

        self.k = 0 #очищаем переменную

        for i in tabs: #перебираем индексы, на которых стоят знаки
            self.primer.insert(i+self.k+1, ' ') #добавляем пробел после этого знака
            self.primer.insert(i+self.k, ' ') #и перед
            self.k += 2 #l нам нужны, потому что, когда мы добавляем 2 пробела, то наш список увеличивается на 2

        self.primer = ''.join(self.primer) #переаводим все в строку
        self.primer = self.primer.split() #и иразделяем эту строку на числа и знаки

        for i in self.primer:
            if i in prior_znaki: #для начала добавим индексы приоритетных знаков
                if len(posled) == 0: #если список пустой
                    posled.append(self.primer.index(i)) #то добавляем 

                else:
                    for l in posled: #перебираем элементы в списке

                        if self.primer[l] in not_prior_znaki: #если там есть знак + или - 
                            posled.insert(posled.index(l), self.primer.index(i)) #то добавляем приоритетный знак перед ним
                            self.flag = True #флаг, чтобы понять, что мы уже вставили индекс
                            break # и выходим из цикла

                    if self.flag is False:
                        posled.append(self.primer.index(i)) #если такого знака нету, то добавляем на последнее место

            if i in not_prior_znaki:
                if len(posled) == 0: #если список пустой
                    posled.append(self.primer.index(i)) #то добавляем на перове место

                else:
                    posled.append(self.primer.index(i))

            self.flag = False #возвращаем его в прошлое значение

        self.result()

        print(float(self.primer[0])) #берем единственный элемент нашего списка и выводим его 

    def result(self):
        for i in posled:
            self.znak = self.primer[i]
            for l in self.primer:
                if l == self.znak: #перебираем знаки приеритета в элементах списка
                    ind = i

                    if self.znak == '+':
                        self.primer = self.sum(self.primer, ind) #присваеваем то, что нам возвращает функция, чтобы использовать это заново
                    elif self.znak == '-':
                        self.primer = self.razn(self.primer, ind)
                    elif self.znak == '*':
                        self.primer = self.proisv(self.primer, ind)
                    elif self.znak == '/':
                        self.primer = self.chast(self.primer, ind)
                    elif self.znak == '^':
                        self.primer = self.stepen(self.primer, ind)

                    break

    def sum(self, b: list, a: int) -> list: #создаем функцию
        self.res = (float(b[a-1]) + float(b[a+1])) #и делаем первое действие
        if len(b) > 3: #если длина списка позволяет
            b.pop(a+1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
            b.pop(a) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
            b.pop(a-1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        else:
            b.clear() #если не позволяет, то очищаем этот список
        b.insert(a-1, self.res) #и на преове место вставляем наш результат
        return b #и возвращаем наш список

    def razn(self, b: list, a: int) -> list:
        self.res = (float(b[a-1]) - float(b[a+1])) #и делаем первое действие
        if len(b) > 3: #если длина списка позволяет
            b.pop(a+1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
            b.pop(a) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
            b.pop(a-1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        else:
            b.clear() #если не позволяет, то очищаем этот список
        b.insert(a-1, self.res) #и на преове место вставляем наш результат
        return b #и возвращаем наш список

    def proisv(self, b: list, a: int) -> list:
        self.res = (float(b[a-1]) * float(b[a+1])) #и делаем первое действие
        if len(b) > 3: #если длина списка позволяет
            b.pop(a+1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
            b.pop(a) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
            b.pop(a-1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        else:
            b.clear() #если не позволяет, то очищаем этот список
        b.insert(a-1, self.res) #и на преове место вставляем наш результат
        return b #и возвращаем наш список

    def chast(self, b: list, a: int) -> list:
        self.res = (float(b[a-1]) / float(b[a+1])) #и делаем первое действие
        if len(b) > 3: #если длина списка позволяет
            b.pop(a+1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
            b.pop(a) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
            b.pop(a-1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        else:
            b.clear() #если не позволяет, то очищаем этот список
        b.insert(a-1, self.res) #и на преове место вставляем наш результат
        return b #и возвращаем наш список

    def stepen(self, b: list, a: int) -> list:
        self.res = (float(b[a-1]) ** float(b[a+1])) #и делаем первое действие
        if len(b) > 3: #если длина списка позволяет
            b.pop(a+1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
            b.pop(a) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
            b.pop(a-1) #то мы обрезаем первые 3 элемента, с которыми мы уже провели действие
        else:
            b.clear() #если не позволяет, то очищаем этот список
        b.insert(a-1, self.res) #и на преове место вставляем наш результат
        return b #и возвращаем наш список

    def __del__(self):
        print('Объект удален')

primerr = Calc(str(input('Введите пример: ')))
primerr.itog_primer()