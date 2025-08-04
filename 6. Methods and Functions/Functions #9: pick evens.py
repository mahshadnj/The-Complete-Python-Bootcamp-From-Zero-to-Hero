'''
Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even.
'''

def myfunc(*args):
    return [arg for arg in args if arg % 2 == 0]
