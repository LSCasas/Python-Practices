#Returns the largest number of the given arguments. In this case, it shows the maximum value between 1, 2, 3, 4 and 5.
def get_max_number(message, *args):
    """
    Returns the maximum number from the given arguments.
    """
    return max(args)
print("The larges number is: ", get_max_number(1,2,3,4,5))


