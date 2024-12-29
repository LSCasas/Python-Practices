#Multiply all numbers given as arguments.
def multiply(*args):
    """
    Multiplies all the given arguments together and returns the result.
    
    Parameters:
        *args: A variable number of numeric arguments to multiply.
    
    Returns:
        int or float: The product of all the arguments.
    """
    start = 1
    for number in args:
        start *= number  
    return start

print("The multiply is:", multiply(1, 2, 3, 4))
