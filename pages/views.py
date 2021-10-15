from django.shortcuts import render
from django.http import HttpResponse
import json

from methods import choose_method
from methods import function_constructor

# Create your views here.


def piece_linear_approximation_show(request):
    return render(request, 'piece_linear_approximation_method.html')


def piece_permanent_approximation_show(request):
    return render(request, 'piece_permanent_approximation_method.html')


def homepage_show(request):
    return render(request, 'home.html')


def render_data_function(data):
    function = function_constructor.get_function(data['function'])
    integ_bottom = float(data['integ_bottom'])
    integ_top = float(data['integ_top'])
    segments = int(data['segments'])
    method = choose_method.get_choose_method(data['method'])
    if choose_method.is_accuracy_method(data['method']):
        accuracy = float(data['accuracy'])
        result = method(function, integ_bottom, integ_top, accuracy, segments)
    result = method(function, integ_bottom, integ_top, segments)
    json_data = json.dumps(data)
    render_data = {'result': result, 'json_data': json_data}
    return render_data


def functions(request):
    if request.method != 'POST':
        return render(request, 'functions.html')
    else:
        data = request.POST
        render_data = render_data_function(data)
        return render(request, 'result.html', context={'data': render_data['json_data'],
                                                       'result': render_data['result']})


def result(request):
    return render(request, 'result.html')
