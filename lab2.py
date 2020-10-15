import math
from array import *
from numpy.core import single, double


def massive_1(alfa):
    mas_a = array('d', [0, 1, 0, 0, 0, 0])
    mas_a[0] = pow(10, alfa)
    mas_a[1] = 1223
    mas_a[2] = pow(10, alfa - 1)
    mas_a[3] = pow(10, alfa - 2)
    mas_a[4] = 3
    mas_a[5] = pow(-10, alfa - 5)
    return mas_a


def massive_2(beta):
    mas_b = array('d', [0, 1, 0, 0, 0, 0])
    mas_b[0] = pow(10, beta)
    mas_b[1] = 2
    mas_b[2] = pow(-10, beta + 1)
    mas_b[3] = pow(10, beta)
    mas_b[4] = 2111
    mas_b[5] = pow(10, beta + 3)
    return mas_b


def mult_1():
    #for alfa in range(-10, 10):
        for beta in range(-10, 20):
            alfa = -10
            mas_a = massive_1(alfa)
            mas_b = massive_2(beta)
            result_1 = single(0)
            result_2 = double(0)
            for i in range(1, len(mas_a)):
                result_1 = single(result_1 + (single(mas_a[i]) * single(mas_b[i])))
                result_2 = double(result_2 + (double(mas_a[i]) * double(mas_b[i])))
            #print(result_1, result_2)
            if result_1 != single(8779):
                print('Одинарная точность:')
                print(f'{beta}//{single(8779) - result_1}')
            else:
                print(f'{beta}//{single(8779) - result_1}')
            if result_2 != double(8779):
                print('Двойная точность:')
                print(f'{beta} // {double(8779) - result_2}')
            else:
                print(f'{beta} //{double(8779) - result_2}')
#

def decision_1(a, b, c):
    Descr = float(b * b - 4 * a * c)
    if Descr > 0:
        x1 = (-1 * b + math.sqrt(Descr)) / (2 * a)
        x2 = (-1 * b - math.sqrt(Descr)) / (2 * a)
        f1 = (a * x1 * x1) + (b * x1) + c
        f2 = (a * x2 * x2) + (b * x2) + c
        print('Первый корень: ', x1)
        print('Второй корень: ', x2)
        print('Первая функция:', f1)
        print('Вторая функция:', f2)
    elif Descr == 0:
        x = float(-1 * b / 2 * a)
        f = (a * x * x) + (b * x) + c
        print('Корень: ', x)
        print('Функция: ', f)
    else:
        print('Нет корней!')


def eps_1():
    eps_comp = single(1)
    eps = single(0.1)
    eps_old = single(0)
    while eps_comp + eps > eps_comp:
        eps_old = single(eps)
        eps = eps * single(0.5)
    print('Машинный эпсилон одинарной точности:', eps_old)

    eps_comp_2 = double(36)
    eps_2 = double(0.1)
    while eps_comp_2 + eps_2 > eps_comp_2:
        eps_old_2 = eps_2
        eps_2 = eps_2 * 0.5
    print('Машинный эпсилон двойной точности:', eps_old_2)


if __name__ == '__main__':
    mult_1()
    #decision_1(3, 8000, 2)
    #eps_1()
