#Solicita dos números, uno mínimo y otro máximo. Si el máximo es menor que el mínimo, muestra un error. 
# Si son válidos, genera una lista de múltiplos de 3 en ese rango.
def read_number(message) -> float:
    """Solicita un número al usuario"""
    is_numeric = False

    while not is_numeric:
        number = input(message)
        is_numeric = number.isnumeric()

    return float(number)

min_number = read_number("Dame un número mínimo de un rango: ")
max_number = read_number("Dame un número máximo de un rango: ")

if max_number < min_number:
    print("Tus datos no son válidos")
else:
    iterator = min_number
    result = []

    while iterator <= max_number:
        if (iterator % 3) == 0:
            result.append(iterator)
        iterator += 1

    print("El resultado es:", result)