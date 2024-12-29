# Write a script that allows sorting the following tuple
pair_numbers = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sort in ascending order by the second element of each tuple
def get_second_value(tupla):
    """Returns the second value of a tuple."""
    return tupla[1]
pair_numbers.sort(key=get_second_value )
print(pair_numbers)
pair_numbers.sort(key=get_second_value, reverse=True)
print(pair_numbers)
