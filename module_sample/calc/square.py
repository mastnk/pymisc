'''
 This module can be accessed from main, because the file name starts with an alphabet.
 See __init__.py
'''

def square(x):
    return x*x

# This function cannot be accessed from main, because the function name starts with '_'
def _square(x):
    return x*x
