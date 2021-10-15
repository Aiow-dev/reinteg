from methods import piece_permanent_approximation
from methods import piece_linear_approximation


def get_choose_method(method):
    methods = {'left_rectangle_method': piece_permanent_approximation.left_rectangle_method, 
               'right_rectangle_method': piece_permanent_approximation.right_rectangle_method,
               'midpoint_rectangle_method': piece_permanent_approximation.midpoint_rectangle_method,
               'trapezoid_method': piece_linear_approximation.trapezoid_method,
               'trapezoid_method_accuracy': piece_linear_approximation.trapezoid_method_accuracy,}
    return methods[method]


def is_accuracy_method(method):
    if method == 'trapezoid_method_accuracy':
        return True
