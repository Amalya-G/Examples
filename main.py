import copy
import random

class LongNumber:

    def __init__(self, number):  # Конструткор класса
        self.SIZE = 30
        if number[0] == '-':   # если число отрицательное
            number = number[:0:-1]
            self.minus = True
            self.digit = [0 if i >= len(number) else int(number[i]) for i in range(self.SIZE)]
        else:
            number = number[::-1]
            self.minus = False
            self.digit = [0 if i >= len(number) else int(number[i]) for i in range(self.SIZE)]

    def __str__(self):   # перезагрузка печати
        ct = 0
        temp_num = self.digit[::-1]

        while ct != self.SIZE:
            if temp_num[ct] != 0:
                break
            ct += 1
        res = "".join(map(str, temp_num[ct:]))

        if self.minus:
            return '-' + res
        else:
            return "0" if res == "" else res

    def __eq__(self, second_num):  # Перезагрузка
        for i in range(self.SIZE-1, -1, -1):
            if self.digit[i] != second_num.digit[i]:
                return False
        return True

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

    def add(self, first_num, second_num):  # Функция сложения
        temp_num = first_num.digit[:]

        for i in range(self.SIZE):  # сложение без учёта переполнения
            temp_num[i] += second_num.digit[i]

        for i in range(self.SIZE - 1):  # перенос для каждого разряда
            if temp_num[i] >= 10:
                temp_num[i] -= 10
                temp_num[i + 1] += 1

        return LongNumber(temp_num[::-1])

    def sub(self, first_num,  second_num):  # Функция вычитания
        temp_num = first_num.digit[:]

        for i in range(self.SIZE):
            temp_num[i] -= second_num.digit[i]

        for i in range(self.SIZE - 1):
            if temp_num[i] < 0:
                temp_num[i] += 10
                temp_num[i + 1] -= 1

        return LongNumber(temp_num[::-1])

    def __add__(self, second_num):  # Перегрузка сложения
        if not self.minus and not second_num.minus:
            res = self.add(self, second_num)
            return res

        elif self.minus and second_num.minus:
            res = self.add(self, second_num)
            res.minus = True
            return res

        elif not self.minus and second_num.minus:
            if self >= second_num:
                res = self.sub(self, second_num)
            else:
                res = self.sub(second_num, self)
                res.minus = True
            return res

        else:
            if self >= second_num:
                res = self.sub(self, second_num)
                res.minus = True
            else:
                res = self.sub(second_num, self)
            return res

    def __sub__(self, second_num):  # Перегрузка вычитания
        if not self.minus and not second_num.minus:
            if self >= second_num:
                res = self.sub(self, second_num)
            else:
                res = self.sub(second_num, self)
                res.minus = True
            return res

        elif self.minus and second_num.minus:
            if self >= second_num:
                res = self.sub(self, second_num)
                res.minus = True
            else:
                res = self.sub(second_num, self)

            return res

        elif not self.minus and second_num.minus:
            res = self.add(self, second_num)
            return res

        else:
            res = self.add(self, second_num)
            res.minus = True
            return res

    def __mul__(self, second_num):
        """Перегрузка умножения"""
        res = LongNumber("0")

        for i in range(self.SIZE):
            for j in range(self.SIZE-i):
                res.digit[i + j] += self.digit[i] * second_num.digit[j]

        for i in range(self.SIZE - 1):
            res.digit[i + 1] += res.digit[i] // 10
            res.digit[i] %= 10

        res.minus = self.minus ^ second_num.minus
        return res

    def __truediv__(self, second_num):
        """Перегрузка деления"""

        if second_num == LongNumber("0"):
            return "Division by zero!"
        elif second_num == LongNumber("1"):
            return self
        elif self == second_num:
            return LongNumber("1")
        elif self == LongNumber("0") or second_num >= self:
            return LongNumber("0")

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

                temp_divisible = LongNumber(temp_divisible[::-1])
                temp_divisor = LongNumber(temp_divisor[::-1])

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

        res = LongNumber(answer)
        if not self.minus and not second_num.minus:
            res.minus = False
        else:
            res.minus = True

        return res


if __name__ == '__main__':
    for i in range(30):
        a1 = random.choice(range(-1000000000, 1000000000))
        b1 = random.choice(range(-1000000000, 1000000000))
        a = LongNumber(str(a1))
        b = LongNumber(str(b1))
    #a = LongNumber("-5349767788945")
    #b = LongNumber("-6574839557832")
        print(f'Тест для чисел {a} и {b}')
        print(f'Сложение равно {a+b}')
        print(f'Разность чисел: {a} и {b} равна {a-b}')
        print(f'Разность чисел: {b} и {a} равна {b-a}')
        print(f'Произведение равно {a*b}')
        print(f'Частное равно {a/b}')
        print(f'Сравнение чисел {a == b}')
        print('Тест окончен')



