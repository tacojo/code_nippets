def head_function(function_name,params):
    map_functions = { 
        'addition': addition, 
        'subtraction': subtraction 
        }
    map_functions[function_name](params)

def addition(params): 
    print(params['x'] + params['y'])
        
def subtraction(params): 
    print(params['x'] - params['y'])

head_function('addition',{'x': 3, 'y': 5})
