import math

def get_function(function_text):
    ready_text = 'lambda x: ' + function_text
    text_replace = ready_text
    functions_replace = {'sqrt': 'math.sqrt', 'sin': 'math.sin',
                         'cos': 'math.cos', 'tg': 'math.tan', '^': '**',
                         'arcsn': 'math.asin', 'arccs': 'math.acos',
                         'pi': 'math.pi', 'e': 'math.e',
                         'atan': 'math.atan', 'snh': 'math.sinh',
                         'csh': 'math.cosh'}
    for replace in functions_replace.keys():
        text_replace = text_replace.replace(replace, functions_replace[replace]
                                            )
    return eval(text_replace)
