def square_number(x):
    return x ** 2

def reverse_string(s):
    return s[::-1]

def invert_boolean(b):
    return not b

def reverse_sequence(seq):
    return seq[::-1]

def swap_dict_keys_values(d):
    if len(set(d.values())) == len(d): 
        return {v: k for k, v in d.items()}
    return d  
    
TRANSFORMATIONS = {
    int: square_number,
    float: square_number,
    str: reverse_string,
    bool: invert_boolean,
    list: reverse_sequence,
    tuple: reverse_sequence,
    dict: swap_dict_keys_values
}

def typeBasedTransformer(**kwargs):
    transformed = {}
    for key, value in kwargs.items():
        transform_func = TRANSFORMATIONS.get(type(value), lambda x: x)
        transformed[key] = transform_func(value)
    return transformed