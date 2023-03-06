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

###########################################################
################### Within a class ########################
###########################################################
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class DynamicFunctionLoop:
    function_name: List
    fn_params: Dict

    def run_list_of_functions(self):
        for fn in self.list_functions:
            head_function(fn, self.params)        

class MyDynamicFunctions(DynamicFunctionLoop):
    def __init__(self, list_functions, params):
        self.list_functions = list_functions
        self.params = params

    def head_function(self, function_name, fn_params):
        map_functions = { 
            'addition': addition, 
            'subtraction': subtraction,
            'multiply': multiply,
            'divide': divide,
            }
        map_functions[function_name](fn_params)

    def addition(self): 
        print(self.params['x'] + self.params['y'])
            
    def subtraction(self): 
        print(self.params['x'] - self.params['y'])

    def multiply(self): 
        print(self.params['x'] * self.params['y'])
            
    def divide(self): 
        print(self.params['x'] / self.params['y'])    

list_functions_1 = ['addition','subtraction']
list_functions_2 = ['multiply','divide']
myparams =  {'x': 2, 'y': 15}

a = MyDynamicFunctions(list_functions_1, myparams)
a.run_list_of_functions()
