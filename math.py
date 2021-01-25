# Perform addition
def add(x,y):
    return x+y
# Perform subtraction
def subtract(x,y):
    if x<y:
        return ERROR
    return x-y
# Perform multiplication
def multiply(x,y):
    return x*y
    
# Perform division
def divide(x,y):
    if y==0:
        return DIV_ERR
    return x/y
def square(x):
    return x*x