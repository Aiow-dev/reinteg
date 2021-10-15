import math
from methods import piece_permanent_approximation


def trapezoid_method(func, a, b, nseg):
    """
    Метод трапеций
    Второй порядок аппроксимации
    """
    dx = 1.0 * (b - a) / nseg
    sum = 0.5 * (func(a) + func(b))
    for i in range(1, nseg):
        sum += func(a + i * dx)

    return sum * dx


def trapezoid_method_accuracy(func, a, b, rtol=1e-8, nseg0=1):
    """Метод трапеций с заданной точностью"""
    nseg = nseg0
    old_ans = 0.0
    dx = 1.0 * (b - a) / nseg
    ans = 0.5 * (func(a) + func(b))
    try:
        for i in range(1, nseg):
            ans += func(a + i * dx)

        ans *= dx
        err_est = max(1, abs(ans))
        while err_est > abs(rtol * ans):
            old_ans = ans
            ans = 0.5 * (
                ans + piece_permanent_approximation.midpoint_rectangle_method(
                    func, a, b, nseg))

            nseg *= 2
            err_est = abs(ans - old_ans)

        return ans
    except ValueError:
        print('Неверно задана функция. Проверьте правильность введенных \
              данных, а также допустимые значения математических функций')
