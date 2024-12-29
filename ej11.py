def my_sort_key(value):
    """
    Returns a sort key based on the type of the value.

    Strings are prioritized before numbers, with case-insensitive comparison for strings.

    Parameters:
        value (str | int | float): The value to generate the sort key for.

    Returns:
        tuple: A key for sorting, where strings are ranked (0, value) and numbers are ranked (1, value).
    """
    if isinstance(value, str):
        return (0, value.lower())
    if isinstance(value, (int, float)):
        return (1, value)

fruits = [
    "bannana",
    "orange",
    "Kiwi",
    "melon",
    1,
    20,
    8.7,
    "Cherry",
    "mango",
    "apple"
]


fruits.sort(key=my_sort_key)


print("Sorted list:", fruits)
