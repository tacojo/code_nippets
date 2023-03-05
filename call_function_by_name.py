def head_function(function_name,params):
    map_functions = { 
        'func1': func1, 
        'func1': func2 
        }
    map_functions[function_name](params)

def func1(params): 
    print(10+params['id'])
        
def func2(params): 
    print(20+params['id'])

head_function('func1',{'id':2})
