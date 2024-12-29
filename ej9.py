#Checks if a number is within a specific range.
def is_in_range(min, max, number):
    """
    Checks if a number is within a specified range (inclusive of min, exclusive of max).
    """
    return number in range(min, max)

print(is_in_range(1,5,4))
print(is_in_range(1,5,20))