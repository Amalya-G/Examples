import copy

class Long_Numb:

    def __init__(self, number):  # Конструткор класса
        self.SIZE = 15
        if number[0] == '-':   # если число отрицательное
            number = number[:0:-1]
            self.negatzn = True
            self.digit = [0 if i >= len(number) else int(number[i]) for i in range(self.SIZE)]
        else:
            number = number[::-1]
            self.negatzn = False
            self.digit = [0 if i >= len(number) else int(number[i]) for i in range(self.SIZE)]
# =========================================================

    def __str__(self):   # перезагрузка печати
        ct = 0
        temp_num = self.digit[::-1]

        while ct != self.SIZE:
            if temp_num[ct] != 0:
                break
            ct += 1
        res = "".join(map(str, temp_num[ct:]))

        if self.negatzn:
            return '-' + res
        else:
            return "0" if res == "" else res

# =========================================================
    def __eq__(self, second_num):  # Перезагрузка
        for i in range(self.SIZE-1, -1, -1):
            if self.digit[i] != second_num.digit[i]:
                return 'Не равны'
        return 'Равны'

# =========================================================

    def __ge__(self, second_num):  # Перегрузка >=
        for i in range(self.SIZE-1, 0, -1):
            if self.digit[i] > second_num.digit[i]:
                return True
            elif self.digit[i] < second_num.digit[i]:
                return False

        if self.digit[0] >= second_num.digit[0]:
            return True
        else:
            return False

# =========================================================

    def add(self, first_num, second_num):  # Функция сложения
        temp_num = first_num.digit[:]

        for i in range(self.SIZE):  # сложение без учёта переполнения
            temp_num[i] += second_num.digit[i]

        for i in range(self.SIZE - 1):  # перенос для каждого разряда
            if temp_num[i] >= 10:
                temp_num[i] -= 10
                temp_num[i + 1] += 1

        return Long_Numb(temp_num[::-1])

# =========================================================

    def __add__(self, second_num):  # Перегрузка сложения
        if not self.negatzn and not second_num.negatzn:  # если оба положительные
            res = self.add(self, second_num)
            return res

        elif not self.negatzn and second_num.negatzn:   # первый полож, второй отриц
            if self >= second_num:
                res = self.sub(self, second_num)
            else:
                res = self.sub(second_num, self)
                res.negatzn = True
            return res

        elif self.negatzn and not second_num.negatzn:  # первый отриц, второй полож
            if self >= second_num:
                res = self.sub(self, second_num)
                res.negatzn = True
            else:
                res = self.sub(second_num, self)
            return res

        else:                                # если оба отрицательные
            res = self.add(self, second_num)
            res.negatzn = True
            return res

# =========================================================
    def sub(self, first_num,  second_num):  # Функция вычитания
        temp_num = first_num.digit[:]

        for i in range(self.SIZE):
            temp_num[i] -= second_num.digit[i]

        for i in range(self.SIZE - 1):
            if temp_num[i] < 0:
                temp_num[i] += 10
                temp_num[i + 1] -= 1

        return Long_Numb(temp_num[::-1])

# =========================================================

    def __sub__(self, second_num):  # Перегрузка вычитания
        if not self.negatzn and not second_num.negatzn:  # если оба положительные
            if self >= second_num:
                res = self.sub(self, second_num)
            else:
                res = self.sub(second_num, self)
                res.negatzn = True
            return res

        elif not self.negatzn and second_num.negatzn:  # если первый полож, второй отриц
            res = self.add(self, second_num)
            return res

        elif self.negatzn and not second_num.negatzn:  # если первый отриц, второй полож
            res = self.add(self, second_num)
            res.negatzn = True
            return res

        else:                              # оба отрицательные
            if self >= second_num:
                res = self.sub(self, second_num)
                res.negatzn = True
            else:
                res = self.sub(second_num, self)

            return res

# =========================================================

    def __mul__(self, second_num):  # Перегрузка умножения
        res = Long_Numb("0")

        for i in range(self.SIZE):
            for j in range(self.SIZE-i):
                res.digit[i + j] += self.digit[i] * second_num.digit[j]

        for i in range(self.SIZE - 1):
            res.digit[i + 1] += res.digit[i] // 10
            res.digit[i] %= 10

        if not self.negatzn and not second_num.negatzn:
            res.negatzn = False
        else:
            res.negatzn = True

        return res

# =========================================================
    def __truediv__(self, second_num):  # Перегрузка деления
        if second_num == Long_Numb('0'):
            return "Делить на ноль нельзя!"
        elif second_num == Long_Numb("1"):
            return self
        elif self == second_num:
            return Long_Numb("1")
        elif self == Long_Numb("0") or second_num >= self:
            return Long_Numb("0")

        else:
            for i in range(self.SIZE-1, -1, -1):  # удаление незначащих нулей
                if self.digit[i] != 0:
                    divisible = self.digit[:i+1]
                    break

            for i in range(self.SIZE-1, -1, -1):  # удаление незначащих нулей
                if second_num.digit[i] != 0:
                    divisor = second_num.digit[:i+1]
                    break

            temp_divisible = copy.deepcopy(divisible)
            answer = ''
            while True:  # цикл деления
                temp_divisor = copy.deepcopy(divisor)
                while len(temp_divisible) > len(temp_divisor):  # добавление нулей справа в делитель
                    temp_divisor.insert(0, 0)
                for i in range(len(temp_divisible)-1, -1, -1):
                    if temp_divisor[i] > temp_divisible[i]:
                        del temp_divisor[0]
                        break
                    elif temp_divisor[i] < temp_divisible[i]:
                        break

                temp_divisible = Long_Numb(temp_divisible[::-1])
                temp_divisor = Long_Numb(temp_divisor[::-1])

                ct = 0
                while True:  # цикл вычитания
                    res = temp_divisible - temp_divisor
                    temp_divisible = res
                    ct += 1
                    if temp_divisor >= temp_divisible:
                        break
                answer += str(ct)

                if second_num >= res:  # условие выхода из цикла деления
                    break

                for i in range(len(res.digit) - 1, -1, -1):  # удаление незначащих нулей в промежуточном результате
                    if res.digit[i] != 0:
                        res = res.digit[:i + 1]
                        break
                temp_divisible = res

        res = Long_Numb(answer)
        if not self.negatzn and not second_num.negatzn:
            res.negatzn = False
        else:
            res.negatzn = True

        return res


if __name__ == '__main__':
    a = Long_Numb("123456789")
    b = Long_Numb("987")
    print(f'Сложение чисел: {a} и {b} равно {a+b}')
    print(f'Разность чисел: {a} и {b} равна {a-b}')
    print(f'Разность чисел: {b} и {a} равна {b-a}')
    print(f'Произведение чисел: {a} и {b} равно {a*b}')
    print(f'Частное чисел: {a} и {b} равно {a/b}')
    print(f'Сравнение чисел: {a} и {b} равно {a == b}')
