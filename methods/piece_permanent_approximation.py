import math


def rectangle_method(func, a, b, nseg, frac):
    """Обобщенный метод прямоугольников"""
    dx = 1.0 * (b-a) / nseg
    sum = 0.0
    xstart = a + frac * dx
    try:
        for i in range(nseg):
            sum += func(xstart + i * dx)

        return sum * dx
    except ValueError:
        print('Неверно задана функция. Проверьте правильность введенных \
              данных, а также допустимые значения математических функций')


def left_rectangle_method(func, a, b, nseg):
    """Метод левых прямоугольников"""
    return rectangle_method(func, a, b, nseg, 0.0)


def right_rectangle_method(func, a, b, nseg):
    """Метод правых прямоугольников"""
    return rectangle_method(func, a, b, nseg, 1.0)


def midpoint_rectangle_method(func, a, b, nseg):
    """
    Метод прямоугольников со средней точкой
    Второй порядок аппроксимации
    """
    return rectangle_method(func, a, b, nseg, 0.5)
