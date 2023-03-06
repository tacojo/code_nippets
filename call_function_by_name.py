###########################################################
################### Standalone func #######################
###########################################################

def head_function(function_name,params):
    map_functions = { 
        'addition': addition, 
        'subtraction': subtraction,
        'multiply': multiply,
        'divide': divide,
        }
    map_functions[function_name](params)

def addition(params): 
    print(params['x'] + params['y'])
        
def subtraction(params): 
    print(params['x'] - params['y'])

def multiply(params): 
    print(params['x'] * params['y'])
        
def divide(params): 
    print(params['x'] / params['y'])    

list_functions_1 = ['addition','subtraction']
list_functions_2 = ['multiply','divide']

def run_list_of_functions(list_functions, params):
    for f in list_functions:
        head_function(f,params)

run_list_of_functions(list_functions_1, {'x': 3, 'y': 5})


